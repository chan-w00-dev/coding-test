#!/usr/bin/env python3
"""프로그래머스 문제 로컬 테스트 러너.

사용법:
    python3 scripts/run_tests.py 배열회전시키기
    python3 scripts/run_tests.py            # 전체 문제 실행
"""
import importlib.util
import json
import sys
import traceback
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "programmers"

GREEN = "\033[92m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"


def load_solution(path: Path):
    spec = importlib.util.spec_from_file_location("solution_mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "solution"):
        raise AttributeError("solution() 함수가 없습니다")
    return mod.solution


def run_one(folder: Path) -> bool:
    sol_path = folder / "solution.py"
    test_path = folder / "tests.json"

    if not sol_path.exists() or not test_path.exists():
        print(f"{GRAY}건너뜀 {folder.name} (solution.py 또는 tests.json 없음){RESET}")
        return True

    data = json.loads(test_path.read_text(encoding="utf-8"))
    cases = data.get("cases", [])

    try:
        solution = load_solution(sol_path)
    except Exception as e:
        print(f"{RED}✗ {folder.name} — 로드 실패: {e}{RESET}")
        return False

    passed = 0
    failed_cases = []

    for i, case in enumerate(cases, start=1):
        args = case["input"]
        if not isinstance(args, list):
            args = [args]
        expected = case["output"]
        try:
            actual = solution(*args)
        except Exception:
            failed_cases.append((i, args, expected, "예외 발생"))
            print(f"{GRAY}{traceback.format_exc()}{RESET}")
            continue

        if actual == expected:
            passed += 1
        else:
            failed_cases.append((i, args, expected, actual))

    total = len(cases)
    if passed == total and total > 0:
        print(f"{GREEN}✓ {folder.name} — {passed}/{total} 통과{RESET}")
        return True

    print(f"{RED}✗ {folder.name} — {passed}/{total} 통과{RESET}")
    for i, args, expected, actual in failed_cases:
        print(f"  케이스 {i}")
        print(f"    입력   : {args}")
        print(f"    기댓값 : {expected}")
        print(f"    실제값 : {actual}")
    return False


def main():
    if not BASE.exists():
        print("programmers/ 디렉토리가 없습니다")
        sys.exit(1)

    targets = []
    if len(sys.argv) > 1:
        name = sys.argv[1]
        matches = [p for p in BASE.rglob(name) if p.is_dir()]
        if not matches:
            print(f"'{name}' 폴더를 찾을 수 없습니다")
            sys.exit(1)
        targets = matches
    else:
        targets = sorted(p for p in BASE.rglob("*") if (p / "solution.py").exists())

    if not targets:
        print("실행할 문제가 없습니다")
        sys.exit(0)

    results = [run_one(t) for t in targets]
    ok = sum(results)
    print()
    print(f"총 {len(results)}문제 중 {ok}문제 통과")
    sys.exit(0 if ok == len(results) else 1)


if __name__ == "__main__":
    main()

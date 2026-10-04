#!/usr/bin/env python3
"""파이썬 문제 로컬 테스트 러너 (programmers, codetree).

사용법:
    python3 scripts/run_tests.py 배열회전시키기
    python3 scripts/run_tests.py            # 전체 문제 실행

programmers 문제는 solution() 함수를 직접 호출해서 검증하고,
codetree 문제는 stdin/stdout으로 solution.py를 실행해서 검증한다.
tests.json의 case["input"]이 리스트면 함수 호출 방식, 문자열이면 stdin 방식으로 판단한다.
"""
import importlib.util
import json
import subprocess
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASES = [ROOT / "programmers", ROOT / "codetree"]

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


def run_function_style(folder: Path, sol_path: Path, cases: list) -> bool:
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


def run_stdin_style(folder: Path, sol_path: Path, cases: list) -> bool:
    passed = 0
    failed_cases = []

    for i, case in enumerate(cases, start=1):
        stdin_data = case["input"]
        expected = case["output"]
        try:
            result = subprocess.run(
                [sys.executable, str(sol_path)],
                input=stdin_data,
                capture_output=True,
                text=True,
                timeout=5,
            )
            actual = result.stdout
            if result.returncode != 0:
                failed_cases.append((i, stdin_data, expected, result.stderr))
                continue
        except subprocess.TimeoutExpired:
            failed_cases.append((i, stdin_data, expected, "시간 초과"))
            continue

        if actual == expected:
            passed += 1
        else:
            failed_cases.append((i, stdin_data, expected, actual))

    total = len(cases)
    if passed == total and total > 0:
        print(f"{GREEN}✓ {folder.name} — {passed}/{total} 통과{RESET}")
        return True

    print(f"{RED}✗ {folder.name} — {passed}/{total} 통과{RESET}")
    for i, stdin_data, expected, actual in failed_cases:
        print(f"  케이스 {i}")
        print(f"    입력   : {stdin_data!r}")
        print(f"    기댓값 : {expected!r}")
        print(f"    실제값 : {actual!r}")
    return False


def run_one(folder: Path) -> bool:
    sol_path = folder / "solution.py"
    test_path = folder / "tests.json"

    if not sol_path.exists() or not test_path.exists():
        print(f"{GRAY}건너뜀 {folder.name} (solution.py 또는 tests.json 없음){RESET}")
        return True

    data = json.loads(test_path.read_text(encoding="utf-8"))
    cases = data.get("cases", [])

    if cases and isinstance(cases[0]["input"], str):
        return run_stdin_style(folder, sol_path, cases)
    return run_function_style(folder, sol_path, cases)


def main():
    bases = [b for b in BASES if b.exists()]
    if not bases:
        print("programmers/ 또는 codetree/ 디렉토리가 없습니다")
        sys.exit(1)

    targets = []
    if len(sys.argv) > 1:
        name = sys.argv[1]
        matches = [p for b in bases for p in b.rglob(name) if p.is_dir()]
        if not matches:
            print(f"'{name}' 폴더를 찾을 수 없습니다")
            sys.exit(1)
        targets = matches
    else:
        targets = sorted(
            p for b in bases for p in b.rglob("*") if (p / "solution.py").exists()
        )

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

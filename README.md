# 코딩테스트 학습 기록

프로그래머스 문제를 풀고, 파이썬 관용구로 다시 짜면서 기록하는 저장소입니다.

## 방식

문제마다 두 번 풉니다.

1. **1차** — 일단 통과시키기
2. **2차** — 슬라이싱, `enumerate`, `Counter` 등 파이썬 관용구로 압축

커밋도 `solve:`와 `refactor:` 두 종류로 남깁니다.

## 진행 현황

**20 / 21** (Lv0, 1차 완료 · 2차 완료)
**13 / 13** (Lv1, 1차 완료 · 2차 완료)

| 문제 | 레벨 | 정답률 | 1차 | 2차 | 익힌 관용구 |
|---|---|---|---|---|---|
| [암호 해독](programmers/lv0/암호해독) | Lv0 | 89% | ✅ | ✅ | 슬라이싱 |
| [인덱스 바꾸기](programmers/lv0/인덱스바꾸기) | Lv0 | 89% | ✅ | ✅ | 튜플 언패킹 스왑 (a, b = b, a) |
| [중복된 문자 제거](programmers/lv0/중복된문자제거) | Lv0 | 87% | ✅ | ✅ | dict.fromkeys |
| [가까운 수](programmers/lv0/가까운수) | Lv0 | 86% | ✅ | ✅ | min(key=) |
| [한 번만 등장한 문자](programmers/lv0/한번만등장한문자) | Lv0 | 86% | ✅ | ✅ | Counter, 컴프리헨션 |
| [최댓값 만들기 (2)](programmers/lv0/최댓값만들기(2)) | Lv0 | 89% | ✅ | ✅ | sorted, 음수 인덱싱 |
| [잘라서 배열로 저장하기](programmers/lv0/잘라서배열로저장하기) | Lv0 | 85% | ✅ | ✅ | range step, 슬라이싱 |
| [2차원으로 만들기](programmers/lv0/2차원으로만들기) | Lv0 | 87% | ✅ | | |
| [모스부호 (1)](programmers/lv0/모스부호(1)) | Lv0 | 86% | ✅ | ✅ | 컴프리헨션 |
| [컨트롤 제트](programmers/lv0/컨트롤제트) | Lv0 | 85% | ✅ | ✅ | enumerate |
| [숨어있는 숫자의 덧셈 (2)](programmers/lv0/숨어있는숫자의덧셈(2)) | Lv0 | 86% | ✅ | ✅ | re.findall, sum() |
| [소인수분해](programmers/lv0/소인수분해) | Lv0 | 84% | ✅ | ✅ | 시행 나눗셈 O(√n) |
| [합성수 찾기](programmers/lv0/합성수찾기) | Lv0 | 88% | ✅ | ✅ | 컴프리헨션 |
| [외계어 사전](programmers/lv0/외계어사전) | Lv0 | 79% | ✅ | ✅ | any(), set 비교 |
| [등수 매기기](programmers/lv0/등수매기기) | Lv0 | 77% | ✅ | ✅ | 컴프리헨션, sum() 제네레이터 |
| [문자열 밀기](programmers/lv0/문자열밀기) | Lv0 | 76% | ✅ | ✅ | 문자열 순환 확인 (A in B+B) |
| [특이한 정렬](programmers/lv0/특이한정렬) | Lv0 | 74% | ✅ | ✅ | sorted(key=), 다중 정렬 기준 |
| [최빈값 구하기](programmers/lv0/최빈값구하기) | Lv0 | 71% | ✅ | ✅ | Counter.most_common() |
| [안전지대](programmers/lv0/안전지대) | Lv0 | 65% | ✅ | ✅ | sum() + 이중 컴프리헨션 |
| [분수의 덧셈](programmers/lv0/분수의덧셈) | Lv0 | 64% | ✅ | ✅ | math.gcd, 정수 나눗셈(//) |
| [평행](programmers/lv0/평행) | Lv0 | 55% | ✅ | ✅ | itertools.combinations, set() 중복 검사 |
| [나누어 떨어지는 숫자 배열](programmers/lv1/나누어떨어지는숫자배열) | Lv1 | 86% | ✅ | ✅ | 컴프리헨션, `or`로 빈 리스트 기본값 처리 |
| [가운데 글자 가져오기](programmers/lv1/가운데글자가져오기) | Lv1 | 85% | ✅ | ✅ | if-elif를 슬라이싱으로 통합 |
| [수박수박수박수박수박수?](programmers/lv1/수박수박수박수박수박수) | Lv1 | 85% | ✅ | ✅ | 문자열 * (조건식)으로 if-else 대체 |
| [문자열 내림차순으로 배치하기](programmers/lv1/문자열내림차순으로배치하기) | Lv1 | 84% | ✅ | ✅ | sorted(reverse=True) + join |
| [문자열 다루기 기본](programmers/lv1/문자열다루기기본) | Lv1 | 82% | ✅ | ✅ | in (a,b,...) 멤버십 체크, return 조건식 직접 반환 |
| [같은 숫자는 싫어](programmers/lv1/같은숫자는싫어) | Lv1 | 80% | ✅ | ✅ | zip으로 한 칸 밀어서 비교 + 컴프리헨션 |
| [최대공약수와 최소공배수](programmers/lv1/최대공약수와최소공배수) | Lv1 | 79% | ✅ | ✅ | math.gcd, math.lcm, return 직접 반환 |
| [이상한 문자 만들기](programmers/lv1/이상한문자만들기) | Lv1 | 77% | ✅ | ✅ | 컴프리헨션 |
| [시저 암호](programmers/lv1/시저암호) | Lv1 | 74% | ✅ | ✅ | 헬퍼 함수 분리 후 컴프리헨션 |
| [두 개 뽑아서 더하기](programmers/lv1/두개뽑아서더하기) | Lv1 | 74% | ✅ | ✅ | itertools.combinations, set() |
| [K번째수](programmers/lv1/K번째수) | Lv1 | 73% | ✅ | ✅ | 컴프리헨션, 튜플 언패킹 |
| [문자열 내 마음대로 정렬하기](programmers/lv1/문자열내마음대로정렬하기) | Lv1 | 73% | ✅ | ✅ | sorted(key=) 다중 정렬 기준(튜플) |
| [카드 뭉치](programmers/lv1/카드뭉치) | Lv1 | 72% | ✅ | ✅ | pop(0)으로 큐 앞 원소 꺼내기 |

## 로컬 테스트

    python3 scripts/run_tests.py <문제 폴더명>
    python3 scripts/run_tests.py              # 전체

## 구조

    programmers/lv<N>/<문제명>/
    ├── problem.md    문제 설명 + 원본 링크
    ├── solution.py   풀이
    ├── tests.json    입출력 예시
    └── note.md       배운 것

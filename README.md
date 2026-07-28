# 코딩테스트 학습 기록

프로그래머스 문제를 풀고, 파이썬 관용구로 다시 짜면서 기록하는 저장소입니다.

## 방식

문제마다 두 번 풉니다.

1. **1차** — 일단 통과시키기
2. **2차** — 슬라이싱, `enumerate`, `Counter` 등 파이썬 관용구로 압축

커밋도 `solve:`와 `refactor:` 두 종류로 남깁니다.

## 진행 현황

**1 / 3** (1차 완료 · 2차 완료)

| 문제 | 레벨 | 정답률 | 1차 | 2차 | 익힌 관용구 |
|---|---|---|---|---|---|
| [암호 해독](programmers/lv0/암호해독) | Lv0 | 89% | ✅ | ✅ | 슬라이싱 |
| [인덱스 바꾸기](programmers/lv0/인덱스바꾸기) | Lv0 | 89% | ✅ | | |
| [중복된 문자 제거](programmers/lv0/중복된문자제거) | Lv0 | 87% | ✅ | | |

## 로컬 테스트

    python3 scripts/run_tests.py <문제 폴더명>
    python3 scripts/run_tests.py              # 전체

## 구조

    programmers/lv0/<문제명>/
    ├── problem.md    문제 설명 + 원본 링크
    ├── solution.py   풀이
    ├── tests.json    입출력 예시
    └── note.md       배운 것

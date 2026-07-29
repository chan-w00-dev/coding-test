# 코딩테스트 학습 기록

프로그래머스 문제를 풀고, 파이썬 관용구로 다시 짜면서 기록하는 저장소입니다.

## 방식

문제마다 두 번 풉니다.

1. **1차** — 일단 통과시키기
2. **2차** — 슬라이싱, `enumerate`, `Counter` 등 파이썬 관용구로 압축

커밋도 `solve:`와 `refactor:` 두 종류로 남깁니다.

## 진행 현황

**5 / 7** (1차 완료 · 2차 완료)

| 문제 | 레벨 | 정답률 | 1차 | 2차 | 익힌 관용구 |
|---|---|---|---|---|---|
| [암호 해독](programmers/lv0/암호해독) | Lv0 | 89% | ✅ | ✅ | 슬라이싱 |
| [인덱스 바꾸기](programmers/lv0/인덱스바꾸기) | Lv0 | 89% | ✅ | | |
| [중복된 문자 제거](programmers/lv0/중복된문자제거) | Lv0 | 87% | ✅ | ✅ | dict.fromkeys |
| [가까운 수](programmers/lv0/가까운수) | Lv0 | 86% | ✅ | ✅ | min(key=) |
| [한 번만 등장한 문자](programmers/lv0/한번만등장한문자) | Lv0 | 86% | ✅ | ✅ | Counter, 컴프리헨션 |
| [최댓값 만들기 (2)](programmers/lv0/최댓값만들기(2)) | Lv0 | 89% | ✅ | ✅ | sorted, 음수 인덱싱 |
| [잘라서 배열로 저장하기](programmers/lv0/잘라서배열로저장하기) | Lv0 | 85% | ✅ | | |

## 로컬 테스트

    python3 scripts/run_tests.py <문제 폴더명>
    python3 scripts/run_tests.py              # 전체

## 구조

    programmers/lv0/<문제명>/
    ├── problem.md    문제 설명 + 원본 링크
    ├── solution.py   풀이
    ├── tests.json    입출력 예시
    └── note.md       배운 것

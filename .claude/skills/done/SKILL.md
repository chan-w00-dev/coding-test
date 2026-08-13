---
name: done
description: 테스트 통과 확인 후 README를 갱신하고 커밋·푸시한다
argument-hint: [문제 폴더명] [solve|refactor]
allowed-tools: Bash(python3:*), Bash(git:*), Read, Write
disable-model-invocation: true
---

1. `python3 scripts/run_tests.py <문제명>` 실행. 실패하면 여기서 멈춘다.

2. `README.md`의 진행 현황표를 갱신한다.
   - 해당 문제 행이 없으면 추가
   - 있으면 상태 갱신 (1차 완료 / 2차 완료)
   - 상단의 진행 개수도 함께 갱신

3. 두 번째 인자에 따라 커밋 메시지를 만든다. 레벨은 문제 폴더 경로(`programmers/lv<N>/...`)에서 그대로 가져온다.
   - `solve` → `solve: <문제 제목> (Lv<N>, <정답률>)`
   - `refactor` → `refactor: <문제 제목> - <note.md에 기록된 관용구>`
   - 인자가 없으면 git 로그를 확인해 판단하고, 애매하면 사용자에게 묻는다

4. 변경된 파일만 스테이징하고 커밋한 뒤 `git push` 한다.

푸시 전에 커밋 메시지를 보여주고 확인을 받는다.

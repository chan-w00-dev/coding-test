---
name: check
description: 해당 문제의 로컬 테스트를 실행한다
argument-hint: [문제 폴더명]
allowed-tools: Bash(python3:*), Read
---

`python3 scripts/run_tests.py <인자>` 를 실행한다.

- 전부 통과하면: 통과 사실만 알리고, `/review`로 넘어가도 좋다고 안내한다.
- 실패하면: 스크립트가 출력한 **실패 케이스의 입력·기댓값·실제값만** 그대로 전달한다.
  원인 분석, 수정 방향, 코드 제안은 하지 않는다.

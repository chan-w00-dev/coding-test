# 외계어 사전

- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120869
- 정답률: 79%

## 문제 설명

PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이가 외계 언어를 학습 중입니다. 알파벳 배열 `spell`과 외계어 사전 `dic`이 주어질 때, `spell`의 모든 알파벳을 정확히 한 번씩 사용한 단어가 사전에 있으면 1을, 없으면 2를 반환하세요.

## 제한사항

- 모든 원소는 소문자 알파벳만 포함
- `spell` 크기: 2~10
- `spell` 각 원소 길이: 1
- `dic` 크기: 1~10
- `dic` 각 원소 길이: 1~10
- 모든 `spell` 원소를 사용해야 함
- 중복 원소 없음

## 입출력 예

| spell | dic | result |
|---|---|---|
| ["p", "o", "s"] | ["sod", "eocd", "qixm", "adio", "soo"] | 2 |
| ["z", "d", "x"] | ["def", "dww", "dzx", "loveaw"] | 1 |
| ["s", "o", "m", "d"] | ["moos", "dzx", "smm", "sunmmo", "som"] | 2 |

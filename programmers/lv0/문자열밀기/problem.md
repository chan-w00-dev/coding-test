# 문자열 밀기

- URL: https://school.programmers.co.kr/learn/courses/30/lessons/120921
- 정답률: 76%

## 문제 설명

문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return하도록 solution 함수를 완성해주세요. 문자열을 민다는 것은 각 문자를 오른쪽으로 한 칸씩 이동시키고 마지막 문자는 맨 앞으로 이동시키는 동작을 의미합니다.

## 제한사항

- 0 < A의 길이 = B의 길이 < 100
- A, B는 알파벳 소문자로 이루어져 있음

## 입출력 예

| A | B | result |
|---|---|---|
| "hello" | "ohell" | 1 |
| "apple" | "elppa" | -1 |
| "atat" | "tata" | 1 |
| "abc" | "abc" | 0 |

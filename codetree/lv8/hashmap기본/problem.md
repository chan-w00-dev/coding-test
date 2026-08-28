# hashmap 기본

- URL: https://edu.codetree.ai/hanyang/class/204/learn/lecture/2071/curated-cards/intro-hashmap-basic/introduction
- 난이도: 레벨 8
- 제한: Python3 1000 ms / 80 MB

## 문제 설명

N개의 명령이 주어졌을 때, 각 명령을 수행하는 프로그램을 작성해보세요. 명령의 종류는 크게 3가지 입니다.

- `add k v` : (k, v) 쌍을 hashmap에 추가합니다. key가 k, value가 v라는 뜻입니다. 이때 만약 동일한 k가 이미 존재한다면, v로 덮어씁니다.
- `remove k` : key가 k인 쌍을 찾아 hashmap에서 제거합니다. 잘못된 입력은 주어지지 않습니다.
- `find k` : key가 k인 쌍이 hashmap에 있는지를 판단합니다. 있다면 해당하는 value를 출력하고, 없다면 None을 출력합니다.

## 입력

첫 번째 줄에는 N이 주어집니다.

두 번째 줄부터는 N개의 줄에 걸쳐 각 명령이 한 줄에 하나씩 주어집니다. 각 명령에 주어지는 key와 value는 전부 숫자입니다. 명령들은 순서대로 수행되어야 합니다.

## 제약 조건

- 1 ≤ N ≤ 100,000
- 1 ≤ 주어지는 수 ≤ 10^9

## 출력

결과를 한 줄에 하나씩 출력합니다.

## 입출력 예시

### 예제 1

입력

```
11
add 3 5
add 10000 1
find 3
find 5
find 10000
add 3 10
find 3
add 7 15
remove 3
remove 7
find 7
```

출력

```
5
None
1
10
None
```

### 예제 설명

명령 find가 주어지는 횟수는 5번으로 3, 4, 5, 7, 11 번째 입니다.

- 3번째 명령이 주어졌을 때, key 3에는 value 5가 들어있습니다.
- 4번째 명령이 주어졌을 때, key 5는 존재하지 않습니다.
- 5번째 명령이 주어졌을 때, key 10000에는 value 1이 들어있습니다.
- 7번째 명령이 주어졌을 때, key 3에는 value 10가 들어있습니다.
- 11번째 명령이 주어졌을 때, key 7은 존재하지 않습니다.

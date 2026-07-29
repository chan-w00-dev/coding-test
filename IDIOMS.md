# 내 파이썬 관용구 사전

## 슬라이싱

## 순회

## 정렬
튜플 정렬 기준 -> min(data, key = lambda x : 1순위, 2순위 ...)

## 자료구조

문자열에서 중복된 문자 제거 -> dict.fromkeys() 활용
dict.fromkeys -> list를 인자로 받고 list 안의 원소를 키로 하는 딕셔너리 생성

collections.Counter - list, string 안의 요소 횟수 세기
## 컴프리헨션

반복문 대신 list = [x for ... in ... if ...]

## 함수형

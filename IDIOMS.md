# 내 파이썬 관용구 사전

## 슬라이싱
list 끝 접근 -> 음수 인덱싱(ex.arr[-1])

## 순회
배열의 요소를 조합하고 싶을 떄 -> itertools.combinations
건너뛰며 순회 -> range(start, stop, step)
리스트의 인덱스와 내용 모두 접근하고 싶을 때 -> enumerate

## 정렬
튜플 정렬 기준 -> min(data, key = lambda x : 1순위, 2순위 ...)

## 자료구조

문자열에서 중복된 문자 제거 -> dict.fromkeys() 활용
dict.fromkeys -> list를 인자로 받고 list 안의 원소를 키로 하는 딕셔너리 생성

collections.Counter - list, string 안의 요소 횟수 세기
## 컴프리헨션

반복문 대신 list = [x for ... in ... if ...]

## 함수형

max()/min()/sum() -> 반복문 대신 제네레이터 표현식으로 가능
any()/all() -> 입력값 중 null값이 하나라도 있냐/ 전체냐 TRUE, FALSE 반환

## 정규표현식

문자열에서 패턴 추출 -> re.findall()
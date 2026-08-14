# 내 파이썬 관용구 사전

## 슬라이싱
list 끝 접근 -> 음수 인덱싱(ex.arr[-1])
문자열 순환(로테이션) 확인 -> B in A+A / str.find() or str.index()
홀/짝 분기 하나의 식으로 통합 -> (len-1)//2 : len//2 + 1 (슬라이싱)
                       -> *(n%2) (홀수면 곱하고 짝수면 아무 일도 일어나지 않음)

## 순회
배열의 요소를 조합하고 싶을 떄 -> itertools.combinations
건너뛰며 순회 -> range(start, stop, step)
리스트의 인덱스와 내용 모두 접근하고 싶을 때 -> enumerate
딕서녀리 key, value 모두 순회 -> dict.items()
리스트에서 연속된 요소 비교 -> arr와 한 칸 밀린 arr zip 활용

## 정렬
튜플 정렬 기준 -> min(data, key = lambda x : 1순위, 2순위 ...)
list.sort() -> None 반환, sorted() -> 새 리스트 반환

## 자료구조

문자열에서 중복된 문자 제거 -> dict.fromkeys() 활용
dict.fromkeys -> list를 인자로 받고 list 안의 원소를 키로 하는 딕셔너리 생성
중복을 허용하지 않은 집합 -> set()
set 비교 -> 동등 비교, 포함 관계 비교
stack -> list.append()/list.pop()으로 구현

collections.Counter - list, string 안의 요소 횟수 세기
                    - Counter.most_common(n) 상위 n개의 튜플 반환

## 컴프리헨션

반복문 대신 list = [x for ... in ... if ...]

## 함수형

max()/min()/sum() -> 반복문 대신 제네레이터 표현식으로 가능
any()/all() -> 입력값 중 null값이 하나라도 있냐/ 전체냐 TRUE, FALSE 반환
math.gcd(a, b) -> 최대공약수, 기약분수 만들 때 사용
return a or b -> a가 falsy 값이면 b 반환


## 정규표현식

문자열에서 패턴 추출 -> re.findall()

## 조건문

여러 값 중 하나와 비교 -> in (a, b, ...)
중첩 if + return True/False -> return <조건문>
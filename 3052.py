numbers = []
for i in range(10):
    numbers.append(int(input()) % 42)
set_num = set(numbers)
print(len(set_num))

'''
집합(set) 자료형
- 생성 방법
1. set(리스트)
2. set("문자열") ex) set("Hello") => {'e', 'H', 'l', 'o'}

- 특징
1. 중복 제거
2. 순서가 없음. unordered
------------------------------------
- 문제를 풀 수 있는 다른 방법
반복문과 not in 연산을 사용하여 해결할 수 있다.
'''
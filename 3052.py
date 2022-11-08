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
'''
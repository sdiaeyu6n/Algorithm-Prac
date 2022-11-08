N=int(input())
numbers=list(map(int,input().split()))
min_num=min(numbers)
max_num=max(numbers)

print(min_num,max_num)

'''
문자열 리스트를 정수형으로 반환하는 방법
1. 입력받을 때 정수형으로 mapping하여 받기
list(map(int, input().split()))
2. 문자열 리스트를 변환하기
list(map(int,strarr))
3. 반복문 이용하기
intarr = [int(i) for i in strarr]
'''
nums=[]
for i in range(9):
    nums.append(int(input()))
output=max(nums)
print(output)
print(nums.index(output)+1)

'''
리스트 요소의 인덱스 찾기
=> 리스트.index(요소)
'''
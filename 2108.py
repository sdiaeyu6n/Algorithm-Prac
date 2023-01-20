import sys,math

N=int(sys.stdin.readline())
num_list=[0]*N
for i in range(N):
    num_list[i]=int(sys.stdin.readline())

#산술평균
# print(round(sum(num_list)/N))
#중앙값
num_list.sort()
# print(num_list[N//2])
#최빈값
number=[0]*8001
for n in num_list:
    # print(n)
    number[n+4000]+=1
print(max(number))
#범위
# print(num_list[-1]-num_list[0])
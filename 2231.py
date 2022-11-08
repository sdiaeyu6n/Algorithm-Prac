N = int(input())
producer = []
numbers=[]

for i in range(N):
    sum=0
    producer=list(str(i))
    sum=int("".join(producer))
    for j in producer:
        sum+=int(j)
    if N==sum:
        numbers.append(i)
if len(numbers)==0:
    print("0")
else: print(min(numbers))
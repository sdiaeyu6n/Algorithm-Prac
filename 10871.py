N,X=map(int, input().split())
A=list(input().split())
output=[]
for i in A:
    if int(i)<X:
        output.append(i)
print(" ".join(output))
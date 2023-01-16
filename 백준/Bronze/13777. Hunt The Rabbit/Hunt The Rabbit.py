import sys
def binary_search(target,array,start,end):
    global output
    if start>end:
        return
    mid = (start+end)//2
    if array[mid]==target:
        output.append(array[mid])
        print(*output)
        return 
    elif array[mid]<target:
        output.append(array[mid])
        return binary_search(target,array,mid+1,end)
    else:
        output.append(array[mid])
        return binary_search(target,array,start,mid-1)

array=[0]*51
for i in range(1,51): 
    array[i]=i

while True:
    num=int(sys.stdin.readline())
    if num==0:
        break
    output=[]
    binary_search(num,array,1,50)
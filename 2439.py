N = int(input())
for i in range(1,N+1):
    output=""
    output+=" "*(N-i)
    output+="*"*i
    print(output)
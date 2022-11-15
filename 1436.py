N = int(input())
name_list=[]
for i in range(2666800):
    if '666' in str(i):
        name_list.append(i)
        if len(name_list)==N:
            print(name_list[N - 1])
            break
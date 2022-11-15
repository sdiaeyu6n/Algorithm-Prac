N = int(input())
name_list = []
i = 0
while len(name_list) <= 10000:
    i += 1
    if '666' in str(i):
        name_list.append(i)
        if len(name_list) == N:
            print(name_list[N - 1])
            break
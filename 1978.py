N = int(input())
num_list = list(map(int, input().split()))

prime = []
for n1 in num_list:
    div_list = []
    for n2 in range(1, n1 + 1):
        if n1 % n2 == 0:
            div_list.append(n2)
    if len(div_list) == 2 and n1 in div_list and 1 in div_list:
        prime.append(n1)
print(len(prime))
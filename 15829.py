L = int(input())
string = list(input())
M = 1234567891
hash_value = 0
i = 0
while (i < len(string)):
    for alp in string:
        hash_value += (ord(alp) - 96) * 31 ** i
        i += 1
print(hash_value % M)
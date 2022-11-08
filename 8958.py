num = int(input())
for i in range(num):
    test_case = list(input())
    score = 0
    contin_o = 0
    for i in test_case:
        if i == 'O':
            contin_o += 1
        else:
            contin_o = 0
        score += contin_o
    print(score)
lengths = [0, 0, 0]
while (True):
    lengths = list(map(int, input().split()))
    if lengths[0] == 0 and lengths[1] == 0 and lengths[2] == 0:
        quit()
    max_length = max(lengths)
    lengths.remove(max_length)
    if lengths[0] ** 2 + lengths[1] ** 2 == max_length ** 2:
        print("right")
    else:
        print("wrong")

'''
프로그램 종료 명령어
quit()
'''
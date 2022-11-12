T = int(input())
for i in range(T):
    room_number = ""
    height = 0
    count = 0
    H, W, N = map(int, input().split())
    if N <= H:
        room_number = str(N) + "01"
    else:
        if N % H == 0:
            height = H
        else:
            height = N % H
        while (N > 0):
            N = N - H
            count += 1
        if len(str(count)) == 1:
            room_number = str(height) + "0" + str(count)
        else:
            room_number = str(height) + str(count)

    print(room_number)
N = int(input())
num_of_rooms = 0
i = 1
while (N > 0):
    N = N - i
    num_of_rooms += 1
    i = 6 *num_of_rooms
print(num_of_rooms)
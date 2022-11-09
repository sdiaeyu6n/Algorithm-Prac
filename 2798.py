N, M = map(int, input().split())
cards = list(input().split())
# diff = []
sum_of_cards = []
for i in cards:
    for j in cards:
        for k in cards:
            if i !=j and j!=k and k!=i \
                    and int(i) + int(j) + int(k) <= M:
                sum_of_cards.append((int(i) + int(j) + int(k)))
print(max(sum_of_cards))
N = int(input())
word_list = []
for i in range(N):
    word_list.append(input())
word_list.sort(key=len)
len_list = []
for word in word_list:
    len_list.append(len(word))

len_set = set(len_list)

word_len_list2 = []
for length in len_set:
    word_len_list1 = []
    for word in word_list:
        if len(word) == length:
            word_len_list1.append(word)
    word_len_list2.append(sorted(set(word_len_list1)))

for w in word_len_list2:
    for o in w:
        print(o)
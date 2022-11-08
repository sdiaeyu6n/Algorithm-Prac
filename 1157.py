word = list(input().upper())
word_set = set(word)
max_list = []
dict_word = {}

for i in word_set:
    dict_word[i] = ''

for i in word_set:
    count = 0
    key_word = ""
    for j in word:
        if i == j:
            count += 1
    dict_word[i] = count
    
for i in dict_word:
    if dict_word[i] == max(dict_word.values()):
        max_list.append(i)

if len(max_list) == 1:
    print(max_list[0])
else:
    print("?")
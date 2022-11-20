word=list(input().upper())
dict_word=dict()
for w in word:
    dict_word[w]=word.count(w)
list_word=list(dict_word.items())
most=max(list_word,key=lambda x:x[1])
result=set()
for i in list_word:
    if i[1] == most[1]:
        result.add(i[0])

if len(result)==1:
    print("".join(result))
else:
    print("?")
word=list(input().upper())
word_dict=dict()
word_set=set(word)
result=[]
for s in word_set:
    count=0
    for w in word:
        if s == w:
            count+=1
    word_dict[s]=count
word_list=list(word_dict.items())
most=max(word_list, key=lambda x:x[1])
for l in word_list:
    if l[1]==most[1]:
        result.append(l[0])

if len(result)==1:
    print("".join(result))
else: print("?")
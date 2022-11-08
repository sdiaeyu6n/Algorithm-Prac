N = int(input())
scores = list(map(int, input().split()))
new_scores=[]
best=max(scores)
worst=min(scores)
for i in scores:
    new_scores.append(i/best*100)
avg_score=sum(new_scores)/N
print(avg_score)
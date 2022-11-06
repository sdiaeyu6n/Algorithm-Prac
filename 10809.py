S = list(input())
output=[]
for i in range(97,123):
    if chr(i) in S:
        output.append(str(S.index(chr(i))))
    else: output.append('-1')
print(" ".join(output))
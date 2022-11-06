S = list(input())
output=[]
for i in range(97,123):
    if chr(i) in S:
        output.append(str(S.index(chr(i))))
    else: output.append('-1')
print(" ".join(output))

'''
구분자.join(리스트): 리스트의 값과 값 사이에 구분자를 넣어서 하나의 문자열로 합쳐준다.
문자열.split(구분자): 문자열을 구분자 단위로 잘라 리스트 형식으로 저장한다. 구분자 기본값은 공백
list(input()): 입력값을 리스트로 저장한다.
'''
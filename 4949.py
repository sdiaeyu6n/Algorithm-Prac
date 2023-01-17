import sys

while True:
    sentence=sys.stdin.readline().rstrip()
    if sentence=='.':
        break
    stack=[]
    check='yes'
    for s in sentence:

        if s == '[' or s=='(':
            stack.append(s)
        elif s ==']':
            if len(stack)==0:
                check='no'
                break
            if stack[-1]== '[':
                stack.pop()
            else: break
        elif s ==')':
            if len(stack)==0:
                check='no'
                break
            if stack[-1] == '(':
                stack.pop()
            else: break

    if len(stack)!=0:
        check='no'

    print(check)
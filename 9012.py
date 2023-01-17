import sys

for i in range(int(sys.stdin.readline())):
    sentence=sys.stdin.readline().rstrip()
    stack=[]
    check='YES'
    for s in sentence:
        if s == '[' or s=='(':
            stack.append(s)
        elif s ==']':
            if len(stack)==0:
                check='NO'
                break
            if stack[-1]== '[':
                stack.pop()
            else: break
        elif s ==')':
            if len(stack)==0:
                check='NO'
                break
            if stack[-1] == '(':
                stack.pop()
            else: break

    if len(stack)!=0:
        check='NO'

    print(check)
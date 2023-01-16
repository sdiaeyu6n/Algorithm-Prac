import sys

A,B,V=map(int,sys.stdin.readline().split())

d1=0
d2=0
eq1=A*d1-B*d1-V # 답=d
eq2=A*(d2+1)-B*d2-V # 답=d+1

while eq1<0:
    d1+=1
    eq1=A*d1-B*d1-V # 답=d

while eq2<0:
    d2+=1
    eq2=A*(d2+1)-B*d2-V # 답=d+1
    
print(min(d1,d2+1))
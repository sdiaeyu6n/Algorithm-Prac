import sys
from sympy import Symbol, solve
import math

d=Symbol('d')
A,B,V=map(int,sys.stdin.readline().split())

eq1=A*d-B*d-V # 답=d
eq2=A*(d+1)-B*d-V # 답=d+1

a1=math.ceil(solve(eq1)[0])
a2=math.ceil(solve(eq2)[0])

print(min(a1,a2+1))
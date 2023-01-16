import sys,math

A,B,V=map(int,sys.stdin.readline().split())

if A>=V:
    print(1)
else:
    print(math.ceil((V-A)/(-B+A)+1))
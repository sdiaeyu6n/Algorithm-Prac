import sys

A,B,V=map(int,sys.stdin.readline().split())
count=1
d=A
while d<V:
    d=d-B+A
    count+=1

print(count)
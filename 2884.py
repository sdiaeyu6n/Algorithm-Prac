H,M=map(int, input().split())
if M-45>=0:
    M=M-45
else:
    M=60-(45-M)
    H=H-1

if H<0:
    H=H+24

print(H,M)
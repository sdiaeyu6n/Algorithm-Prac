n1,n2,n3,n4,n5 = map(int, input().split())

verif_number = (n1**2+n2**2+n3**2+n4**2+n5**2)%10
print(verif_number)
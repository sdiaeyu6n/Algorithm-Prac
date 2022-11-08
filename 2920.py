notes = list(map(int, input().split()))
if sorted(notes,reverse=False) == notes:
    print("ascending")
elif sorted(notes,reverse=True) == notes:
    print("descending")
else:
    print("mixed")

'''
정렬
1. 리스트.sort(reverse=False) 
=> 아무것도 return하지 않는다. 리스트는 정렬되어 저장된다.
2. sorted(리스트, reverse=True)
=> 정렬된 리스트를 return한다. 정렬여부 확인시에는 sorted 사용하기.
'''
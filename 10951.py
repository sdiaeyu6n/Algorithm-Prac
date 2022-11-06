while(1):
    try: 
        A,B=map(int, input().split())
        print(A+B)
    except:
        break


'''
try except: 예외 처리
=> try except를 이용한 예외처리를 하지 않게 되면,
런타임 에러가 발생한다. (EOFError)
'''
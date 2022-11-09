while (1):
    number = input()
    if number == '0':
        quit()
    else:
        if number == number[::-1]:
            print('yes')
        else:
            print('no')
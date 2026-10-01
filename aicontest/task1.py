def f(bd, login, c):
    
    if login in bd:
        login = login[:-1] + f'{c}'
        f(bd, login, c+1)
        print('f', c, login)
    else: return login

n = int(input())
B = []
for i in range(n):
    l = input()
    if l in B :
        l = l + '1'
        l = f(B, l, 2)
        print(l)
        B.append(l)

    else:
        print('OK')
        B.append(l)
    

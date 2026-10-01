a, b = map(int, input().split())
s = int(b[int(a[1])-1])
c = 0
for i in b:
    j = int(i)
    if j > 0 and j >= s: 
        c+=1

    else:
        break

print(с)
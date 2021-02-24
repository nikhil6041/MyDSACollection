x , y , z = [] , [] , []
n = int(input())
for _ in range(n):
    x1 , y1 , z1 = list(map(int,input().split()))
    x.append(x1)
    y.append(y1)
    z.append(z1)
sx = sum(x)
sy = sum(y)
sz = sum(z)

if sx == 0 and sy == 0 and sz == 0:
    print("YES")
else:
    print("NO")

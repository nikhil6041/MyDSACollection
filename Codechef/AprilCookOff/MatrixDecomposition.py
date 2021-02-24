import numpy as np

T = int(input())

modulo = 10**9+7
for t in range(T):
    N , A = list(map(int,input().split()))
    p = [A]
    for i in range(1,N):
        val = p[i-1]
        x = (val*(A**i))**(2*i+1)
        x %= modulo
        p.append(x)
    print(sum(p)%modulo)

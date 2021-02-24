T = int(input())
for _ in range(T):
    N = int(input())
    f = list(map(int,input().split()))
    distance = 0
    currentgasoline = f[0]
    for i in range(1,n):
        currentgasoline += 1
        distance += 1
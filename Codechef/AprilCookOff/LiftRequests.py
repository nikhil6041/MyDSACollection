T = int(input())

for t in range(T):
    N , Q = list(map(int,input().split()))
    initialStart = 0
    totalLiftsTravelled = 0
    for i in range(Q):
        f , d = list(map(int,input().split()))
        d1 = abs(initialStart - f)
        d2 = abs(f-d)
        totalLiftsTravelled += (d1+d2)
        initialStart = d
    print(totalLiftsTravelled)
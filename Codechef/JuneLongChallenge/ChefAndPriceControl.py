T = int(input())

for testcases in range(T):

    N , K = list(map(int , input().split()))

    P = list(map(int , input().split()))

    revenueLost = 0

    for iteration in range(N):

        if P[iteration] > K :

            revenueLost += (P[iteration] - K)
    
    print(revenueLost)
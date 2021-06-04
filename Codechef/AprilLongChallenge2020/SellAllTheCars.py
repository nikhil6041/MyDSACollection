import numpy as np
T = int(input())
modulo = 10**9 + 7
for t in range(T):

    N = int(input())
    P = list(map(int,input().split()))
    P.sort(reverse = True)

    profit = 0

    depreciation = 0

    for i in range(len(P)):

        if P[i] - depreciation >= 0:

            P[i] -= depreciation
        
        else:

            P[i] = 0

        depreciation += 1
    
    for i in range(len(P)):

        profit = (profit%modulo + P[i]%modulo)%modulo
        
    print(profit%modulo)

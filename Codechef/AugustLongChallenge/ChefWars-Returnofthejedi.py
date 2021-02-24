T  = int(input())

for t in range(T):

    H , P = list(map(int , input().split()))

    while P > 0:

        H -= P 
        P = P//2 
    # print(H ,P)
    if H > P:
        print(0)
    else:
        print(1)
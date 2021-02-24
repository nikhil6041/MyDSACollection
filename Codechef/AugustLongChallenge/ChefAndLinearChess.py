T = int(input())

for t in range(T):

    N , K = list(map(int , input().split()))
    P = list(map(int , input().split()))

    flg = True

    NumberOfMoves = 10**9
    for i in range(N):

        if K%P[i] == 0:
            flg = False
            NumberOfMoves = min(NumberOfMoves , K//P[i])

    if flg:
        print(-1)
    else:
        print(K//NumberOfMoves)

    
T = int(input())

for testcases in range(T):

    N , Q = map(int,input().split())

    X , Y = [] , []

    for line in range(N):

        x , y = map(int , input().split())

        X.append(x)

        Y.append(y)
    
    Xq , Yq = [] , []

    for query in range(Q):

        xq , yq = map(int , input().split())

        Xq.append(xq)

        Yq.append(yq)

    print(*X , *Y)

    print(*Xq , *Yq) 
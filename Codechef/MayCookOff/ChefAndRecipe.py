def fun(A,N):

    dc = {}
    for i in range(N):
        if A[i] not in dc.keys():
            dc[A[i]] = A.count(A[i])

    flg  = False
    for k1 in dc.keys():
        for k2 in dc.keys():
            if k1 != k2 and dc[k1] == dc[k2]:
                return False 
    d = {}
    for i in range(N):
        if A[i] not in d.keys():
            d[A[i]] = [i]
        else:
            d[A[i]].append(i)
    
    for k in d.keys():
        l = d[k]
        n = len(l)
        for i in range(1,n):
            if l[i] - l[i-1] > 1:
                return False
    return True
        

T = int(input())

for t in range(T):

    N = int(input())

    A = list(map(int,input().split()))

    if fun(A,N):
        print("YES")
    else:
        print("NO")
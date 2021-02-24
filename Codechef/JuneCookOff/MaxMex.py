def check(a,n,m):
    
    a.sort()

    l = [v for v in a if v < m]
    # print(l)
    if len(l) <= n - 1:
        return len(l) + 1
    return -1


T = int(input())

for t in range(T):

    N , M = list(map(int , input().split()))

    A  = list(map(int , input().split()))

    print(check(A,N,M))
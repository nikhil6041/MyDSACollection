# T = int(input())
# for _ in range(T):
#     N , M = list(map(int,input().split()))
#     A = list(map(int,input().split()))
#     B = list(map(int,input().split()))
#     A.sort()
#     B.sort(reverse=True)
#     # print(A)
#     # print(B)
#     i = 0
#     upperLimit = min(N,M)
#     while sum(A) <= sum(B) and i < upperLimit:
#         A[i] , B[i] = B[i] , A[i]
#         i += 1 
#     if sum(A) > sum(B):
#         print(i)
#     else:
#         print(-1)

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    # suma,sumb=0,0
    a=list(map(int,input().split(maxsplit=n-1)))
    b=list(map(int,input().split(maxsplit=m-1)))
    suma=sum(a)
    sumb=sum(b)
    a=sorted(a)
    b=sorted(b,reverse=True)
    # print(b)
    # revb=b[::-1]
    if(suma>sumb):
        print(0)
    else:
        j = 0
        flg = True
        while j < min(n,m) and sum(a) <= sum(b):
            a[j],b[j] = b[j],a[j]
            j += 1
        if sum(a)>sum(b):
            flg = False
            print(j)
        else:
            print(-1)
           
           

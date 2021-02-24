def fun(num):
    oddCountNum , evenCountNum = 0 , 0
    if num%2 == 0:
        oddCountNum , evenCountNum = num//2 , num//2
    else:
        oddCountNum , evenCountNum = num//2 + 1 , num//2
    
    return (oddCountNum,evenCountNum)

T = int(input())
## sum of two no.s x and y is even only when either both are even or both are odd
for _ in range(T):
    A , B = list(map(int,input().split()))
    oddCountA , evenCountA  = fun(A)
    oddCountB , evenCountB = fun(B)
    totalCount = oddCountA*oddCountB + evenCountA*evenCountB
    print(totalCount)
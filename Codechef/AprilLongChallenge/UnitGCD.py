from math import gcd
# def fun(n):
#     if n == 1:
#         return [[1]]
#     B = [True]*(n+1)
#     L = [[2*i] for i in range(1,n//2+1)]
#     # print(L)
#     for i in range(2,len(B),2):
#         B[i] = False
        
#     for i in range(n//2):
#         valueList  = L[i]
#         l = []
#         for k in range(1,n+1):
#             flg = True
#             for j in range(len(valueList)):
#                 val = valueList[j]
#                 if gcd(val,k) != 1:
#                     flg = False
#                     break 
#             if flg and B[k]:
#                 B[k] = False
#                 L[i].append(k)
#     return L                
def fun(n):
    l = []
    if n>1:
        for i in range(1,n,2):
            l.append([i,i+1])
        if n%2!=0:
            l[0].append(n)
    else:
        l.append([1])
    # print(l)
    return l
T = int(input())

for t in range(T):
    N = int(input())
    l = fun(N)
    print(len(l))
    for i in range(len(l)):
        val = l[i]
        print(len(val),end = " ")
        print(*val)

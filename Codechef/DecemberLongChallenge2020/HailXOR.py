# def search(arr,val,idx,start):
#     midx = idx
#     mval = arr[idx]^val
#     for i in range(start+1,len(arr)):
#         cval = arr[i]^val 
#         if cval < mval:
#             midx = i 
#     return midx

# from math import log2
# T = int(input())
# for _ in range(T):
#     N , X = list(map(int,input().split()))
#     A = list(map(int,input().split()))
#     i , j = 0 , 1
#     l = []
#     ## if x > n print the last one else print the nth one
#     while j < N:
#         if A[i] != 0:
#             p = int(log2(A[i]))
#             val = 2**p
#             A[i] ^= val 
#             A[j] ^= val
#             l.append(A[:]) 
#         else:
#             i += 1
#             j = i+1
        
#     # print(l)
#     if X >= N:
#         print(*l[len(l)-1])
#     else:
    
#         print(l[X-1])
from math import log2

T = int(input())
for _ in range(T):
    N , X = list(map(int,input().split()))
    A = list(map(int,input().split()))
    i , k = 0 , X
    while k > 0 and i < N - 1:
        flag = False;
        p = int(log2(A[i]))
        final_val = 2**p
        A[i] ^= final_val
        j = i + 1

        while j < N:
            if A[j]^final_val < A[j]:
                A[j] ^= final_val
                flag = True
                break
            j += 1

        if flag == 0 :
            A[N - 1] ^= final_val

        while A[i] <= 0 and i < N:
            i += 1

        k -= 1

    z = k + 1

    if z > 0 and ((N < 3) and (z%2 == 0)):
        A[N - 1] ^= 1
        A[N - 2] ^= 1
    
    print(*A)





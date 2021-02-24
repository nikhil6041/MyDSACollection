# import time 
# start = time.time()
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    B = list(set(A))
    B.sort()
    if len(B) == 1:
        print(0)
    elif len(B) == 2:
        print(2*(B[1]-B[0]))
    else:
        if len(B)%2 == 0:
            mid1 = len(B)//2 - 1 
            val1 = abs(B[-1] - B[mid1]) + abs(B[mid1] - B[0]) + abs(B[-1] - B[0])
            mid2 = mid1 + 1
            val2 = abs(B[-1] - B[mid2]) + abs(B[mid2] - B[0]) + abs(B[-1] - B[0])
            val = max( val1 , val2 )
            print(val)
        else:
            mid = len(B)//2
            print( abs(B[-1] - B[mid]) + abs(B[mid] - B[0]) + abs(B[-1] - B[0]))
# print(time.time() - start)
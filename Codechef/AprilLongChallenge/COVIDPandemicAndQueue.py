T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    idx = [ i for i,v in enumerate(A) if v == 1]
    flg = True   
    for i in range(1,len(idx)):
        if idx[i] - idx[i-1] < 6:
            flg = False
            break 
    if flg:
        print("YES")
    else:
        print("NO")
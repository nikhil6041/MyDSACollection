
t = int(input())

for _ in range(t):
    n,x,k = list(map(int,input().split()))

    ## forward journey
    # flg = False
    # for i in range(0,n+2,k):
    #     if i == x or n+1 - i == x:
    #         flg = True
    #         break        
    if x%k == 0 or (n+1-x)%k == 0:
        print("YES")
    else:
        print("NO")
























            # ## backward journey
    # for i in range(n+1,-1,-k):
    #     if i == x:
    #         flg = True
    #         break        

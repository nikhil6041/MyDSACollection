T = int(input())
for _ in range(T):
    N , K = list(map(int,input().split()))
    H = list(map(int,input().split()))
    arr = sorted(H,reverse=True)
    s1,s2 = 0 , 0 
    c = 0
    # print(arr)
    while len(arr) >= 2:
        if s1 < K:
            s1 += arr[0]
            c += 1 
        if s2 < K:
            s2 += arr[1]
            c += 1
        # print(arr[0],arr[1])
        del arr[:2]
        if s1 >= K and s2 >= K:
            break
    if 0 < len(arr) < 2 and (s1 < K or s2 < K) :
        if s1 < s2:
            s1 += arr[0]
        else:
            s2 += arr[0]
        c += 1
    if s1 >= K or s2 >= K:
        print(c)
    else:
        print(-1)

# def check1(arr):
#     for i in range(len(arr)):
#         if (i+1) != abs(arr[i]):
#             return False 
#     return True 

# def check2(arr,k):
#     c = 0
#     s = 0
#     for i in range(len(arr)):
#         s += arr[i]
#         if s > 0:
#             c += 1
#     if c == k :
#         return True 
#     else:
#         return False 
    

T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    arr = list(range(1,N+1))
    if N == K:
        print(*arr)
    else:
        mx_permissible_steps = N - K
        step_count = 0
        if N%2 == 0:
            fstart , estart , step = 0 , N-1  , 2
            while step_count < mx_permissible_steps :   
                # forward pass
                if fstart < estart:
                    arr[fstart] = -arr[fstart]
                    fstart += step 
                # backward pass
                else:
                    arr[estart] = -arr[estart]
                    estart -= step
                step_count += 1
        else:
            fstart , estart , end ,step = 0 , N-2 ,N-1, 2
            while step_count < mx_permissible_steps :   
                # forward pass
                if fstart <= end:
                    arr[fstart] = -arr[fstart]
                   # print(f"arr[fstart] => {arr[fstart]} , fstart => {fstart}")
                    fstart += step 
                # backward pass
                else:
                    arr[estart] = -arr[estart]
                    #print(f"arr[estart] => {arr[estart]} , estart => {estart}")
                    estart -= step
                step_count += 1
        print(*arr)
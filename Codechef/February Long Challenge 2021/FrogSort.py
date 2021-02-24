T = int(input())
for _ in range(T):
    N = int(input())
    W = list(map(int,input().split()))
    L = list(map(int,input().split()))

    ## making a zipped array of tuples having each tuple as (weight of the frog , distance the frog can jump , current position of the frog )
    zipped_arr = sorted(zip(W,L,range(1,N+1)) , key=lambda x:x[0])
    # print(zipped_arr)
    total_hits = 0
    for idx , el in enumerate(zipped_arr):

        weight , distance , current_position = el
        
        if idx == 0:
            continue
        else:
            prev_weight , prev_dist , prev_pos = zipped_arr[idx-1]
            # print(prev_weight , prev_dist , prev_pos)
            # print(weight , distance , current_position)
            if prev_pos >= current_position:
                while current_position <= prev_pos:
                    current_position += distance
                    total_hits += 1
            zipped_arr[idx] = (weight , distance , current_position)
        # print(zipped_arr)
        # print(idx,current_position)
    print(total_hits)
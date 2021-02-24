T = int(input())

for _ in range(T):
    N , K , x , y = list(map(int,input().split()))
    finalx,finaly = x , y
    if x == y:
        finalx , finaly = N , N
    else:
        c  = 0
        while c < K:
            if  c%4 == 0: 
                    ## (N,0)
                diff = N - finalx
                    ## (X+,Y+)
                finaly = finaly + diff
                finalx = finalx + diff
            elif c%4 == 1:
                    ## (N,N)
                diff = N - finaly
                    ## (X-,Y+)
                finalx = finalx - diff 
                finaly = finaly + diff
            elif c%4 == 2:
                    ## (0,N)
                diff = finalx 
                    ## (X-,Y-)
                finalx = finalx - diff 
                finaly = finaly - diff
            elif c%4 == 3:
                    ## (0,0)
                diff = finaly 
                    ## (X+,Y-)
                finalx = finalx + diff
                finaly = finaly - diff
            # l.append((finalx,finaly))
            if finalx == finaly:
                finalx , finaly = N , N
                break
            c += 1
        # print(l)
        # finalx , finaly = l[(K-1)%4]

    print(finalx,finaly)
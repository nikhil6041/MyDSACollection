T = int(input())

for _ in range(T):
    N , X = list(map(int,input().split()))

    d = {}

    for i in range(N-1):
        u , v = list(map(int,input().split()))

        if u not in d.keys():
            d[u] = [v]
        else:
            d[u].append(v)
        
    print(d)

    vals = {k:0 for k  in range(1,N)}
    vals[1] = X 

    for k in d.keys():
        if k == 1:
            for el in d[k]:
                l = []
                if el in d.keys():
                    l.append(el)
                
    print(vals)
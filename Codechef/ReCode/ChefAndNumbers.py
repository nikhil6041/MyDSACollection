T = int(input())

for t in range(T):

    N = int(input())

    A = list(map(int , input().split()))

    Aunique = list(set(A))
    d = {}
    for ele in Aunique:

        tmp = [ j for j in range(len(A)) if A[j] == ele ]

        # print(tmp)
        c = 1
        inc = 1
        lastSelected = tmp[0]
        for i in range(1,len(tmp)):
            if tmp[i] - lastSelected > 1:
                lastSelected = tmp[i]
                c += 1
            else:
                continue
            # print(inc)
            
        # print(ele , c)
        if c not in d:
            d[c] = ele
        else:
            d[c] = min(ele,d[c])
    mx = max(d.keys())
    print(d[mx])
T = int(input())

for t in range(T):

    S = input()

    d = {}

    for ch in S:

        if ch not in d.keys():

            d[ch] = S.count(ch)

    flg = True
    
    for k in d.keys():

        if d[k]%2!=0:
            flg = False
            break
    
    if flg:
        print(1)
    else:
        print(-1)
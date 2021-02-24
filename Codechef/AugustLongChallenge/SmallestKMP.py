T = int(input())

for t in range(T):

    S = input()

    P = input()

    diS = {}

    for ch in set(S):
        diS[ch] = S.count(ch)
    
    diP = {}

    for ch in set(P):
        diP[ch] = P.count(ch)

    difference = {}

    for k in diS.keys():
        difference[k] = diS[k] - diP.get(k,0)

    res = ''

    for k in sorted(difference.keys()):

        res += difference[k]*k

    # print(res)

    l = []
    l.append(P+res)
    for i in range(len(res)):

        if res[i] < P[0]:
            continue
        elif res[i] == P[0]:
            x = res[:i] + P + res[i:]
            l.append(x)
        else:
            l.append(res[:i]+P + res[i:])
            break
    l.append(res+P)
    # print(l)
    print(min(l))
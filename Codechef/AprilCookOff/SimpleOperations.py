T = int(input())

for t in range(T):
    S = input()
    R = input()
    idx = []
    for i in range(len(S)):
        if S[i]!=R[i]:
            idx.append(i+1)
    print(idx)
    k = 1
    s = -idx[0]
    for i in range(1,len(idx)):
        if idx[i] - idx[i-1] > 0:
            k += 1
            s += (idx[i] + 1)
    print(k)
    print(s)
### we have two cases when K is more minimize the no. of tables
### and in the other case use as much as tables to avoid conflicts
### total cost =  cost of table + no. of guests who can invlove in an argument



T = int(input())

for t in range(T):

    N , K = list(map(int , input().split()))

    F = list(map(int , input().split()))

    d = {i:F.count(i)-1 for i in set(F)}
    l = []

    i = 0

    tmp = []

    while i < N:

        if F[i] not in tmp:
            tmp.append(F[i])
        else:
            l.append(tmp)
            tmp = [F[i]]

        i += 1
    l.append(tmp)
    print(l)
    print(d)
    # initialCost = K*len(l)
    # for k in d.keys():
        
    # print(initialCost)

    # print((str(F)[1:-1]).replace(',',""))

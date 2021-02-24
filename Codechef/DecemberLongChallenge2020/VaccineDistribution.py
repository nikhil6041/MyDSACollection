T = int(input())
for _ in range(T):
    N , D = list(map(int,input().split()))
    a = list(map(int,input().split()))
    ## people at risk are those whose age >= 80 or age <= 9 
    atRisks , notAtRisks = [] , []
    for el in a:
        if el>=80 or el<=9:
            atRisks.append(el)
        else:
            notAtRisks.append(el)
    numOfDays = 0

    for i in range(0,len(atRisks),D):
        numOfDays += 1
    for i in range(0,len(notAtRisks),D):
        numOfDays += 1
    print(numOfDays)

D1,V1,D2,V2,P = list(map(int,input().split()))

numVaccines = 0
startDay = 1
numDays = 0
while numVaccines < P:

    if (D1 - numDays) <= 0:
        numVaccines += V1 
    if (D2 - numDays) <= 0:
        numVaccines += V2

    numDays += 1

print(numDays-1)
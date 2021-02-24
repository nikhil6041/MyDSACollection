T = int(input())

for t in range(T):

    # input

    N = int(input())

    A = list(map(int , input().split()))

    # logic
    distances = []
    for i in range(1,N):
        distances.append(A[i] - A[i-1])
    
    c = 1
    ArrayOfCounts  = []
    for i in range(len(distances)):
        val = distances[i]

        if val <= 2:
            c += 1
        else:
            ArrayOfCounts.append(c)
            c = 1
    ArrayOfCounts.append(c)
    print(ArrayOfCounts)
    #output
    print(min(ArrayOfCounts) , max(ArrayOfCounts))
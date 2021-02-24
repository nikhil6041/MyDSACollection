T = int(input())

for testcase in range(T):

    N = int(input())

    S = list(map(int , input().split()))

    totalSkippedStrings = 0

    for idx in range(1,N):

        diff = abs(S[idx] - S[idx-1])
        if diff > 0:
            diff -= 1
        totalSkippedStrings += diff
        
    print(totalSkippedStrings)
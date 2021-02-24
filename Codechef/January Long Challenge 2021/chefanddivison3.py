T = int(input())
for _ in range(T):
    N , K , D = list(map(int,input().split()))
    A = list(map(int,input().split()))
    totalProblems = sum(A)
    print(min(D,totalProblems//K))
T = int(input())

for t in range(T):

    L , R = list(map(int , input().split()))

    diff = R - L

    print(2*diff)
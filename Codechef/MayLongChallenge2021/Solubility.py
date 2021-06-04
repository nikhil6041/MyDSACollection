t = int(input())

for _ in range(t):
    x,a,b = list(map(int,input().split()))
    finalval = (a + (100-x)*b)*10
    print(finalval)
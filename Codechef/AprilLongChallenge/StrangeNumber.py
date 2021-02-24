import math
def Factors(n): 
    l  = [] 
    while n%2 == 0:
        l.append(2)
        n = n//2
    for i in range(3,math.ceil(math.sqrt(n)),2):
        while n%i == 0:
            l.append(i)
            n = n//i
    if n>2:
        l.append(n)
    return l    

T = int(input())

for t in range(T):
    x , k = list(map(int,input().split()))
    L = Factors(x)
    if len(L) < k:
        print(0)
    else:
        print(1)

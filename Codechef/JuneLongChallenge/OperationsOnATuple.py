  
T = int(input())

for testcases in range(T):

    p , q , r = map(int , input().split())

    a , b , c = map(int , input().split())

    stepCount = 0
    

    while p < a or q < b or r < c:

        flga , flgb , flgc = True , True , True

        if a%p == 0 and  a!=p and flga:

            p *= 2

            flga = False
        
        if b%q == 0 and b!=q and flgb:

            q *= 2

            flgb = False

        if c%r == 0 and c!=r and flgc:

            r *= 2

            flgc = False
        
        if a%p != 0 and flga:

            p = a

            flga = False 
        
        if b%q != 0 and flgb:

            q = b

            flgb = False 

        if c%r != 0 and flgc:

            r = c

            flgc = False 

        print(p,q,r)
        stepCount += 1

    print(stepCount)
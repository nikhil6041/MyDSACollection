def FindDigitSum(num):
    s = 0
    while num!=0 :
        s += num%10
        num //= 10
    return s

T = int(input())

#a -> Chef
#b -> Morty

for testcase in range(T):

    N = int(input())

    chefScore , mortyScore = 0 , 0

    for iter in range(N):

        a , b = list(map(int , input().split()))

        sa , sb = FindDigitSum(a) , FindDigitSum(b)

        if sa > sb:

            chefScore += 1

        elif sb > sa:

            mortyScore += 1
        
        else:

            chefScore += 1
            mortyScore += 1

    if chefScore > mortyScore:
        print(0,chefScore)
    
    elif mortyScore > chefScore:
        print(1,mortyScore)

    else:
        print(2 , chefScore)


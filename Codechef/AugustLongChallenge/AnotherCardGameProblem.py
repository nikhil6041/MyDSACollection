# 0 -> Chef Wins
# 1 -> Rick Wins
# player with fewer digits wins
# if digits are equal then Rick cheats and wins

T = int(input())

for t in range(T):

    Pc , Pr = list(map(int , input().split()))

    Pcq , Pcrem = Pc//9 , Pc%9

    Prq ,Prrem = Pr//9 , Pr%9

    # print(Pcq , Pcrem)

    # print(Prq , Prrem)
    digitChef , digitRick = Pcq , Prq

    if Pcrem!=0:
        digitChef += 1
    if Prrem!=0:
        digitRick += 1

    if Pcq == Prq:
        print(1,digitRick)
    elif Pcq > Prq:
        print(1,digitRick)
    elif Prq > Pcq:
        print(0,digitChef)
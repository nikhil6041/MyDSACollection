T = int(input())

for testcases in range(T):

    N = int(input())

    A = list(map(int , input().split()))

    flg = True

    MoneyWithChef = {5:0,10:0}

    for i in range(N):

        value = A[i]

        if value == 10:

            MoneyWithChef[value - 5] -= 1

            if MoneyWithChef[value - 5] < 0:
                flg = False
                break

            MoneyWithChef[value] += 1
        
        elif value == 15:

            tmp1 = MoneyWithChef[value - 5] - 1
            tmp2 = MoneyWithChef[value - 10] - 2

            if tmp1 < 0 and tmp2 < 0:
                
                flg = False
                break

            elif tmp1 >= 0:

                MoneyWithChef[value - 5] -= 1

            elif tmp2 >= 0:

                MoneyWithChef[value - 10] -= 2

        else:

            MoneyWithChef[value] += 1

    
    if flg:
        print("YES")
    else:
        print("NO")

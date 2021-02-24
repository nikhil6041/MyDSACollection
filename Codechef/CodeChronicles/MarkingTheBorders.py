T = int(input())

for testcases in range(T):

    a , b , L , R = list(map(int , input().split()))

    s = 0 

    c = 0

    if a > R :
        c = 0
    else:

        while s <= R:

            s += a

            c += 1

            if s > R:
                break

            s += b
            c += 1
    print(c)
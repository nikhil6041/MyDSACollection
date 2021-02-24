T = int(input())

for testcases in range(T):

    S = input()
    
    N = len(S)
    
    i , count = 0 , 0

    while i < N - 1 :

        if (S[i] == 'x' and S[i+1] == 'y') or (S[i] == 'y' and S[i+1] == 'x'):

            count += 1

            i += 2

        else:

            i += 1

    print(count)
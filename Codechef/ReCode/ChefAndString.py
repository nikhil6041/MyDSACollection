T = int(input())

def L(X,N):

    return X[1:N] + X[0]

def R(X,N):

    return X[N-1] + X[:N-1]

for t in range(T):

    S = input()

    S1 = S[::-1]
    s1a = L(S1,len(S1))
    s1b = R(S1,len(S1))

    if  s1a == S and s1b == S:
        print("YES")
    else:
        print("NO")

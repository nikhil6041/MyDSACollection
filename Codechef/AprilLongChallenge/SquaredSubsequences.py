# If N is odd, then it is (N+12)2−(N−12)2.

# If N is divisible by four, then it is (N4+1)2−(N4−1)2.
modulo = 10**9+7
def fun(l):
    # for i in range(len(L)):
    #     if L[i]%2!=0 :
    #         l.append(i)
    #     elif L[i]%4 == 0:
    #         l.append(i)
    # for i in range(len(L)):
    #     val = L[i]
    #     for j in range(i+1,len(L)):
    #         val  = (val*L[j])%modulo
    #         if val%4 == 0 or val%2!=0:
    #             l.append((i,j))
    # for i in range(len(L)):
    #     val = L[i]
    #     if val%4 == 0 or val%2!=0:
    #         l.append((i,i))
    val = 1
    for i in range(len(l)):
        val = (val*l[i])%modulo
    if val%4==0 or val%2!=0:
        return True 
    return False

T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    c = 0
    # print(idxO,idxF)
    for i in range(N):
        for j in range(i,N):
            l = A[i:j+1]
            if fun(l):
                c += 1
    print(c)
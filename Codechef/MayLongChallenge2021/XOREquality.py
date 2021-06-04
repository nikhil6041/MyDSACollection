m = 10**9 + 7

def power(base, exp,m):
    """ Fast power calculation using repeated squaring """
    if exp < 0:
        return 1 / power(base, -exp)
    ans = 1
    while exp:
        if exp & 1:
            ans =  (ans*base)%m
        exp >>= 1
        base = (base*base)%m
    return ans

t = int(input())

for _ in range(t):
    n = int(input())
    val = power(2,n-1,m)
    print(val)
    # l = [ i for i in range(0,2**n,2) if i%2 == 0]
    # print(f"max => {2**n}")
    # print(l)
    # print(len(l))
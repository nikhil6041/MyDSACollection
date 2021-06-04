T = int(input())

for _ in range(T):
    N , M = list(map(int,input().split()))

    # brute force soln.
    s = set()
    s1 , s2 = set() , set()
    for a in range(1,N+1):
        for b in range(a+1,N+1):
            # print(f"a => {a} , b => {b} ")
            # print((M%a)%b)
            # print((M%b)%a)
            s1.add(M%a)
            s2.add(M%b)
            # print((M%a)%b)
            # print((M%b)%a)
            if (M%a)%b == (M%b)%a:
                s.add((a,b))
    print(s)

    # ## assuming the inital soln. of the form a + N*b = M
    # s = []
    # for a in range(1,N+1):
    #     b = M-a 
    #     if b%(N) == 0:
    #         s.append(a)
    #         s.append(b)
    # print(s)

    # ## now, we have a*x + b*y = M
    # ## we will find out all possible soln.s of this eqn.
    # a , b = s
    # soln = set() 
    # for x in range(1,N+1):
    #     y = M - a*x
    #     if y%b == 0:
    #         soln.add((x,y))
    # print(soln)
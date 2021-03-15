from math import ceil, log2

T = int(input())
for i in range(T):
    C = int(input())
    d = -1
    if C == 1:
        d = 1
    elif C%2 == 0:
        d = ceil(log2(C+1))
    else:
        d = ceil(log2(C))
    # print(f"d => {d}")
    a = 2**(d-1) - 1
    b = a^C 
    print(a*b)
    # maxVal = -1
    # for v in range(0,val//2):
    #     temp = v^C 
    #     maxVal = max(maxVal,temp*v)
    #     print(f" u => {temp} v => {v} pro => {maxVal}")

    # # pro = -1
    # # for v in range(0,val):
    # #     for u in range(0,val):
    # #         if u^v == C:
    # #             # print(u,v)
    # #             tmp = u*v
    # #             pro = max(pro,tmp)
    # #             # print(f" u => {u} v => {v} pro => {pro}")
    # # print(pro)
    # print(maxVal)
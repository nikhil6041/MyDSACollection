def update(hr,min,flg):
    if flg == 'PM':
        if hr != 12:
            hr += 12 
    else:
        if hr == 12:
            hr -= 12 
    return (hr,min)
 
T = int(input())
for _ in range(T):

    ptime , pflg  = input().split()
    # print(ptime , pflg )
    phr , pmin = map(int,ptime.split(':'))
    
    phr , pmin = update(phr,pmin,pflg)

    # print(f"phr => {phr} , pmin => {pmin}")        
    
    result = ''

    N = int(input())
    
    for i in range(N):

        ltime , lflg , rtime , rflg = input().split()
        
        ## extracting lower limit vals
        lhr , lmin = map(int,ltime.split(':'))

        lhr , lmin = update(lhr,lmin,lflg)

        # print(f"lhr => {lhr} , lmin => {lmin} , flg => {lflg}")

        ## extracting upper limit vals        
        rhr , rmin = map(int,rtime.split(':'))

        rhr , rmin = update(rhr,rmin,rflg)

        # print(f"rhr => {rhr} , rmin => {rmin} , flg => {rflg}")

        # print(f"lhr<=phr  == {lhr<=phr}")
        # print(f"phr<=rhr == {phr<=rhr}")
        # print(f"lmin<=pmin == {lmin<=pmin}")
        # print(f"pmin<=rmin == {pmin<=rmin}")
        ## initializing the flags
        l_flg , r_flg = False , False

        ## main code logic

        ## lower limit
        
        ## check for the hours
        if lhr < phr:
            l_flg = True 
        elif lhr == phr:
            if lmin <= pmin:
                l_flg = True 

        ## upper limit

        ## check for the hours
        if phr < rhr:
            r_flg = True
        elif phr == rhr:
            if pmin <= rmin:
                r_flg = True 

        # print(l_flg , r_flg)

        if l_flg and r_flg:
            result += '1'
        else:
            result += '0'
    print(result)
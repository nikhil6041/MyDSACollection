# # 1: if the position is reachable, and the game has drawn or one of the players won.
# # 2: if the position is reachable, and the game will continue for at least one more move.
# # 3: if the position is not reachable.

# def check_ltor_diagonal(l):
    
#     i , j = 0 , 0
#     n_rows = 3
#     n_cols = 3
#     s = []

#     while i < n_rows and j < n_cols:
#         s.append(l[i][j])
#         i+=1
#         j+=1
    
#     if '_' not in s and len(s) == 3 and len(set(s)) == 1:
#         return list(set(s))[0] 
#     else:
#         return False

# def check_rtol_diagonal(l):

#     n_rows = len(l)
#     n_cols = len(l[0])
#     i , j = 0 , n_cols - 1
#     s = []

#     while i < n_rows and j >= 0:
#         s.append(l[i][j])
#         i += 1
#         j -= 1
    
#     if '_' not in s and len(s) == 3 and len(set(s)) == 1:
#         return list(set(s))[0] 
#     else:
#         return False

# def check_row(l):

#     i , j = 0 , 0
#     n_rows = 3
#     n_cols = 3
#     dec = []
#     while i < n_rows:
#         s = []
#         j = 0
#         while j < n_cols:
#             s.append(l[i][j])
#             j += 1
#         if '_' not in s and len(s) == 3 and len(set(s)) == 1:
#             dec.append(list(set(s))[0])
#         i += 1
#     if len(dec) == 1:
#         return dec[0]
#     else:
#         return False

# def check_column(l):
    
#     i , j = 0 , 0
#     n_rows = len(l)
#     n_cols = len(l[0])
#     dec = []
#     while j < n_cols:
#         s = []
#         i = 0
#         while i < n_rows:
#             s.append(l[i][j])
#             i += 1
#         # print(s)
#         if '_' not in s and len(s) == 3 and len(set(s)) == 1:
#             dec.append(list(set(s))[0])
#         j += 1
#     if len(dec) == 1:
#         return dec[0]
#     else:
#         return False

# def count_x_y(l):
#     cntx , cnto = 0 , 0
#     for el in l:
#         cntx += el.count('X')
#         cnto += el.count('O')
#     diff = cntx - cnto
#     if 0 <= diff < 2 :
#         return True 
#     else:
#         return False 
# def count_(l):
#     c = 0
#     for el in l:
#         c += el.count('_')
#     return c 

# def count_remaining_moves(l):
#     cnt = 0
#     for el in  l:
#         cnt += el.count('_')
#     return cnt

# t = int(input())
# for _ in range(t):
#     l = []
#     for i in range(0,3):
#         l.append(list(input()))
  
#     # for el in l:
#     #     print(el)
#     # print(check_column(l))
#     # print(check_ltor_diagonal(l))
#     # print(check_rtol_diagonal(l))
#     # print(check_row(l))
    
#     results = [check_ltor_diagonal(l) , check_rtol_diagonal(l) , check_row(l) , check_column(l)]
#     cnt = results.count(False)
#     if len(results) - cnt == 0:
#         print(3)
#     # check reachability
#     # reachability means it shouldn't violate the rules
#     # we can't hv two winners at the same time
#     print(results)



debug_flg = False
t = int(input())
for _ in range(t):
    l = []
    for i in range(0,3):
        l.append(list(input()))

    flgX , flgO = False , False 
    
    ## check row
    for el in l:
        if el.count('X') == 3 :
            flgX = True 
        elif el.count('O') == 3:
            flgO = True

    if debug_flg:
        print(f"Row check {flgX , flgO}")

    ## check column
    i , j = 0 , 0
    n_rows , n_cols = len(l) , len(l[0])

    
    while i < n_cols:
        j = 0
        cx , co = 0 , 0    
        while j < n_rows:
            val = l[j][i]
            if val == 'X':
                cx += 1
            elif val == 'O':
                co += 1
            # print(l[j][i],end=" ")
            j += 1
        # print()
        if cx == 3:
            flgX = True 
        if co == 3:
            flgO = True
        i += 1


    if debug_flg:
        print(f"Column check {flgX , flgO}")

    ## check l to r diagonal
    i , j = 0 , 0
    tmp = []
    while i < n_rows and j < n_cols:
        tmp.append(l[i][j])
        i += 1
        j += 1
    if tmp.count('X') == 3:
        flgX = True 
    elif tmp.count('O') == 3:
        flgO = True 

    if debug_flg:
        print(f"L to R diagonal check {flgX , flgO}")

    ## check r to l diagonal
    i , j = 0 , n_cols - 1
    tmp = []
    while i < n_rows and j >= 0:
        tmp.append(l[i][j])
        i += 1
        j -= 1
    if tmp.count('X') == 3:
        flgX = True 
    elif tmp.count('O') == 3:
        flgO = True 

    if debug_flg:
        print(f"R to L diagonal check {flgX , flgO}")

    ##check reachability
    cntX , cntO = 0 , 0
    for el in l:
        cntX += el.count('X')
        cntO += el.count('O')

    if debug_flg:
        print(f"countX => {cntX} , countO => {cntO}")

    if 0 <= cntX - cntO <= 1:    
        
        if (flgX and flgO) or (cntX > cntO and flgO) or (cntO >= cntX and flgX):
            print(3)
        elif flgX or flgO or (cntX + cntO == 9):
            print(1)
        else:
            print(2)

    else:
        print(3)
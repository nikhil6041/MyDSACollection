# def seriesSummation(n):

#     return ( n*(n + 1) )//2

def findValue(row,column,diagonalValue,mxV):

    diff = abs(row - column)

    if mxV%2 != 0:
            
        if row < column:
            diagonalValue += diff 
        else:
            diagonalValue -= diff

    else:
        
        if row < column:
            diagonalValue -= diff 
        else:
            diagonalValue += diff


    return diagonalValue

T = int(input())

for t in range(T):

    row , column = list(map(int , input().split()))

    mxV = max(row,column)

    diagonalValue = 1 + mxV*(mxV-1)
    
    
    # diagonalValue = 1 + 2*seriesSummation(mxV-1)

    # print(diagonalValue)

    print(findValue(row , column , diagonalValue , mxV))


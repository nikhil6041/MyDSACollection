def highestPowerOf2(n):  
  
    return (n & (~(n - 1))) 

T = int(input())
    
for testcases in range(T):

    TS = int(input())

    val = highestPowerOf2(TS)

    TS = TS//val

    print(TS//2)

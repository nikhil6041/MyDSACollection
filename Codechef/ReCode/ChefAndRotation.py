def CeilIndex(A, l, r, key): 
  
    while (r - l > 1): 
      
        m = l + (r - l)//2
        if (A[m] >= key): 
            r = m 
        else: 
            l = m 
    return r 
   
def LongestIncreasingSubsequenceLength(A, size): 
  
    # Add boundary case, 
    # when array size is one 
   
    tailTable = [0 for i in range(size + 1)] 
    len = 0 # always points empty slot 
   
    tailTable[0] = A[0] 
    len = 1
    for i in range(1, size): 
      
        if (A[i] < tailTable[0]): 
  
            # new smallest value 
            tailTable[0] = A[i] 
   
        elif (A[i] > tailTable[len-1]): 
  
            # A[i] wants to extend 
            # largest subsequence 
            tailTable[len] = A[i] 
            len+= 1
   
        else: 
            # A[i] wants to be current 
            # end candidate of an existing 
            # subsequence. It will replace 
            # ceil value in tailTable 
            tailTable[CeilIndex(tailTable, -1, len-1, A[i])] = A[i] 
          
   
    return len

T = int(input())

for t in range(T):

    N = int(input())
        
    A = list(map(int,input().split()))

    m = 1
    ln = LongestIncreasingSubsequenceLength(A,N)

    while True:
        A1 = A*(m + 1)
        ln1 = LongestIncreasingSubsequenceLength(A1,(m + 1)*N)
        if ln1 <= ln:
            break
        else:
            ln = ln1
        m += 1
    print( m )
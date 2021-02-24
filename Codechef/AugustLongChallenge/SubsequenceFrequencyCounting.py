def mostFrequent(arr, n): 
  
    # Insert all elements in Hash. 
    HashTable = dict() 
    for i in range(n): 
        if arr[i] in HashTable.keys(): 
            HashTable[arr[i]] += 1
        else: 
            HashTable[arr[i]] = 1
  
    # find the max frequency 
    max_count = 0
    res = -1
    for i in HashTable:  
        if (max_count < HashTable[i]):  
            res = i 
            max_count = HashTable[i] 
          
    return res   

def printSubsequences(arr, n ,d) : 
  
    # Number of subsequences is (2**n -1) 
    opsize = 2**n 
  
    # Run from counter 000..1 to 111..1 
    for counter in range( 1, (int)(opsize)) : 
        tmp = [] 

        for j in range(0, n) : 
              
            # Check if jth bit in the counter 
            # is set If set then print jth  
            # element from arr[] 
            if (counter & (1<<j)) : 
                # d[j] += 1
                tmp.append(arr[j])
        # print(f" counter -> {counter} ")
        frequentValue = mostFrequent(tmp,len(tmp))
        d[frequentValue] += 1
        # print(tmp)   
              
        
    return d
  
T = int(input())

for t in range(T):

    N = int(input())

    A = list(map(int , input().split()))

    d = {k:0 for k in range(1,N+1)}

    di = printSubsequences(A,N,d)
    for k in sorted(di.keys()):
        print(di[k] , end=" ")
    print()
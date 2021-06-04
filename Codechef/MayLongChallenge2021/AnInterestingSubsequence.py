# from math import gcd
# mx_val = 2*10^6 + 1
# gc = []
# for i in range(1,mx_val+1):
#     ai = 
#     gc.append(gcd())

# for i in range(1,)
# T = int(input())

# for _  in range(T):
#     k = int(input())

#     l = []
#     # ## brute force soln.
#     # for i in range(1,2*k+2):
#     #     val = k + i**2
#     #     l.append(val)
#     # #     print(val,end=" ")
#     # s = 0
#     # for i in range(1,len(l)):
#     #     s += gcd(l[i-1],l[i])
#     # print(s)
#     # # print()
#     # g = {}
#     # for i in range(1,len(l)):
#     #     # print(f" x = {l[i-1]} , y = {l[i]} , gcd =  {gcd(l[i-1],l[i])}")
#     #     g[ ( l[i-1] , l[i] ) ] = gcd(l[i-1],l[i])
    
#     # # print(l)
#     # # print(g)
#     # for k in g.keys():
#     #     print(g[k] , end = " ")
#     # print()


MAX = 2*10^6 + 1
phi = [0] * MAX
def computeTotient():
    phi[1] = 1
    for i in range(2, MAX):
        if not phi[i]:
            phi[i] = i - 1
            for j in range(i << 1, MAX, i):
                if not phi[j]:
                    phi[j] = j
                phi[j] = ((phi[j] // i) * 
                          (i - 1))
  
# Precomputes result 
# for all numbers 
# till MAX
def sumOfGcdPairs():
      
    # Precompute all phi value
    computeTotient()
  
    for i in range(MAX):
          
        # Iterate throght all 
        # the divisors of i.
        for j in range(2, MAX):
            if i * j >= MAX:
                break
            result[i * j] += i * phi[j]
  
    # Add summation of 
    # previous calculated sum
    for i in range(2, MAX):
        result[i] += result[i - 1]
  
# Driver code
# Function to calculate 
# sum of all the GCD pairs
sumOfGcdPairs()
result = [0] * MAX

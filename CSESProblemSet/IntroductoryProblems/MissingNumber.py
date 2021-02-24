from functools import reduce
n = int(input())
numbers = list(map(int , input().split()))
s = reduce((lambda x,y:x+y),numbers)
print((n*(n+1))//2 - s) 
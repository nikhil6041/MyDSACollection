def CreateBlocks(n,b):
    l = []
    for i in range(0,n,b):
        x = [k for k in range(i,i+b) if k!=n ]
        l.append(x)
    return l

def FindBlock(b,xi):
    for i in range(len(b)):
        bl = b[i]
        if xi in bl:
            return i
    return -1

def CountBlocks(b,x):
    idx = FindBlock(b,x[0])
    previousBlock = idx 
    c = 1
    for i in range(1,len(x)):
        val = x[i]
        currentBlock = FindBlock(b,val)
        if currentBlock != previousBlock:
            c += 1
            previousBlock = currentBlock

    return c

T = int(input())

for t in range(T):

    N , B , M = list(map(int,input().split()))

    x = list(map(int,input().split()))

    Blocks = CreateBlocks(N,B)

    # print(Blocks)

    print(CountBlocks(Blocks,x))

sizeOfArray = int(input())
array = list(map(int , input().split()))

c = 0

for i in range(1,sizeOfArray):
    if array[i] < array[i-1]:
        c += (array[i-1] - array[i])
        array[i] = array[i-1]
print(c)

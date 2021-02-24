matrix = []
for i in range(5):
    l = list(map(int,input().split()))
    matrix.append(l)

i1 , j1 = -1 , -1

for i in range(5):
    for j in range(5):
        val = matrix[i][j]
        if val == 1:
            i1 , j1 = i+1 , j+1 
            break 

print( abs(i1-3) + abs(j1-3))    
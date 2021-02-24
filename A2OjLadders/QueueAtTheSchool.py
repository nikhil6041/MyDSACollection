n , t = list(map(int,input().split()))
s = list(input())
c = 0
i = 0
while c < t :
    if i < n - 1:
        if s[i] == 'B' and s[i+1] == 'G':
            s[i] , s[i+1] = 'G' , 'B'
    i += 1
    c += 1
print(''.join(s))
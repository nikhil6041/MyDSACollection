s = input()
prev = s[0]
c = 0
mxl = 0
for i in range(len(s)):
    curr = s[i]
    if prev == curr:
        c += 1
    else:
        c = 1
    prev = curr
    mxl = max(mxl,c)

print(mxl)
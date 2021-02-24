t = int(input())
for _ in range(t):
    n = int(input())
    b = input()
    attended = b.count('1')
    # # print(attended)
    # totalpossibility = attended + 120 - n
    # # print(totalpossibility)
    # # print(totalpossibility/120)
    if (attended + (120-n))/120 >= 0.75:
        print("YES")
    else:
        print("NO")
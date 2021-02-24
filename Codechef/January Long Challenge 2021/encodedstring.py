english_letters = list('abcdefghijklmnop')

def get_string(s):
    temp  = english_letters.copy()
    n = len(temp)
    txt = ''
    c = 0
    for i in range(0,len(s)):
        n = len(temp)
        if s[i] == '0':
            temp = temp[:n//2]
            c += 1
        elif s[i] == '1':
            temp = temp[n//2:]
            c += 1
        if c%4 == 0 and i!=0:
            txt = txt + ''.join(temp)
            c = 0
            temp = english_letters.copy()
        # print(f"i = {i} , temp = {temp} , txt = {txt}")
    return txt

# def get_string(si):
#     for i in range(0,len(si),4):
#         if si[i] == '0':
#             pass 
#         elif si[i] == '1':
#             pass 
#         if si[i+1] == '0':
#             pass
#         elif si[i+1] == '1':
#             pass 
#         if si[i+2] == '0':
#             pass
#         elif si[i+2] == '1':
#             pass 
#         if si[i+3] == '0':
#             pass 
#         elif si[i+3] == '1':
#             pass

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    print(get_string(S))

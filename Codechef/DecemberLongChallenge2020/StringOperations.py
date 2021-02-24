
def getSubstrings(s, n):
    l = set()
    for i in range(n):
        temp=""
        for j in range(i,n):
            temp+=s[j]
            if temp.count('1')%2 == 0:
                l.add(temp)
            # print(temp)
    return l

def reverseStrings(l):
    s = []
    for el in l:
        s.append(el)
        s.append(el[::-1])
    return s

T = int(input())
for _ in range(T):

# initializing string  
    test_str = input()
    
    # printing original string  
    # print("The original string is : " + str(test_str)) 
    l = getSubstrings(test_str,len(test_str))
    print(l) 
    # s = reverseStrings(l)
    # print(s)
    # print(len(s))   
    

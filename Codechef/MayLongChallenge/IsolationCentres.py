def AnswerQuery(D,C):
    size = 0
    for key in D.keys():
        size += max(0,D[key] - C)
    return size
T = int(input())

for t in range(T):

    N , Q = list(map(int , input().split()))

    S = input()

    #preprocess the string 
    D = {}
    for character in S:
        if character not in D.keys():
            D[character] = S.count(character)

    for query in range(Q):

        C = int(input())
        print(AnswerQuery(D,C))
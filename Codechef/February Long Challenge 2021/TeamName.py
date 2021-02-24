T = int(input())
for _ in range(T):
    N = int(input())
    S = input().split()
    words = {}

    ## constructing our word set
    for word in S:
        if word[0] not in words.keys():
            words[word[0]] = [word]
        else:
            words[word[0]].append(word)

    # print(words)

    ## base conditions
    keys = list(words.keys())


    if len(keys) == 1:
        print(0)
    else:
        count_unique = 0
        for key in keys:
            if len(words[key]) == 1:
                count_unique += 1
        ## all possible permutations taking 2 at a time ( nP2  = (n-2)*(n-1))
        print(count_unique*(count_unique-1))
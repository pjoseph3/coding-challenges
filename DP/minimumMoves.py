

def minMoves(s1,s2):

    return helper(s1,s2,0,0)


def helper(s1,s2,s1i,s2i):

    if s1i == len(s1):
        return len(s2) - s2i
    if s2i == len(s2):
        return len(s1) - s1i


    if s1[s1i] is not s2[s2i]:
        insert = helper(s1,s2,s1i,s2i+1)
        delete = helper(s1,s2,s1i+1,s2i)
        replace = helper(s1,s2,s1i+1,s2i+1)
        return 1 + min(insert,delete,replace)
    else:
        same = helper(s1,s2,s1i+1,s2i+1)
        return same


def main(s1,s2):

    print(minMoves(s1,s2))

if __name__ == '__main__':
    s1 = "Sade"
    s2 = "Paul"

    main(s1,s2)+
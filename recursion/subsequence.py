global count
def countSubseq(small,large):
    global count
    count = 0

    helper(small, large, "")
    return count



def helper(small, large, word):
    global count
    if len(large) == 0:
        if small == word:
            count += 1
        return


    helper(small, large[1:], word + large[0])
    helper(small, large[1:], word)

def main(k,j):

    print(countSubseq(k,j))


if __name__ == '__main__':
    k = "abc"
    j = "abc"
    main(k,j)
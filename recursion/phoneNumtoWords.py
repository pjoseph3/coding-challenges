def phoneNum(num1):

    arr = [[''],['a','b','c'], ['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    results = []
    numArr = []
    for s in num1:
        numArr.append(arr[int(s)])
    helper(numArr,"",results)

    return results

def helper(numArr, word, results):
    if len(numArr) == 0:
        results.append(word)
        return results
    else:
        for str in numArr[0]:
            helper(numArr[1:],word + str,results)
    return results
def main(s):

        print(phoneNum(s))

if __name__ == '__main__':

    s = "1267178"
    main(s)
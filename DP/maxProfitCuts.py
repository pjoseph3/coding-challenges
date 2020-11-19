
memoize = []
def rodCut(prices,L):

    global memoize

    for i in range(L+2):
        memoize.append(-1)

    return helper(prices,L,0)


def helper(prices, L, currPrice):
    global memoize

    if L == 0:
        return currPrice

    if memoize[L] is not -1:
        return memoize[L]

    maxProfit = currPrice
    for i in range(1,L+1):

        maxProfit = max(helper(prices,L-i,currPrice+prices[i]),maxProfit)

    memoize[L] = maxProfit
    return maxProfit




def main(arr,L):

    print(rodCut(arr,L))

if __name__ == '__main__':

    arr = [0,1,3,3,8,8,10] # ans is 11, memoize not working
    main(arr,6)
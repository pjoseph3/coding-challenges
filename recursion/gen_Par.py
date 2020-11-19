def gen_Par(k):
    results = []
    left = k
    right = k
    helper(left, right, "",results)
    return results



def helper(left, right, string, results):
    if left == 0 and right == 0:
        results.append(string)
        return

    if left == right:
        helper(left - 1, right, string + '(',results)
    else:
        if left > 0: helper(left - 1, right, string + '(',results)
        helper(left, right - 1, string + ')', results)
    return results

def main(k):

    print(gen_Par(k))


if __name__ == '__main__':
    k = 3
    main(k)
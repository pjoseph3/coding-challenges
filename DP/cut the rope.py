def max_product_from_cut_pieces(n):
    #
    # Write your code here.
    #

    return helper(n, 0, 1)


def helper(n, prev, mult):

    if n == 0:
        if prev != mult:
            return mult
        else:
            return 0

    result = mult

    for i in range(1, n+1):
        result = max(helper(n - i, i, i * mult), result)

    return result


def main(n):

    print(max_product_from_cut_pieces(n))

if __name__ == '__main__':


    main(13)
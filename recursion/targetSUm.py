def check_if_sum_possible(arr, k):

    return helper(arr, k, 0, 0)



def helper(arr, k, arrSum, count):
    if arrSum == k and count > 0:
        return True

    if len(arr) == 0:
        return False

    r1 = helper(arr[1:], k, arrSum + arr[0], count + 1)
    if r1 is True:
        return True
    r2 = helper(arr[1:], k, arrSum, count)
    return r2

def main(arr,k):

    print(check_if_sum_possible(arr,k))


if __name__ == '__main__':
    arr = [10,20,0]
    k = 0
    main(arr,k)
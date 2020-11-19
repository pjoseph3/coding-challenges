def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    if n % 2 == 0:
        middle = (n//2)
    else:
        middle = (n//2) + 1

    Left = merge_sort(arr[0:middle])
    Right = merge_sort(arr[middle:n])
    return merge(Left, Right)

def merge(Left, Right):

    i = 0
    j = 0
    returnArr = []

    while i < len(Left) and j < len(Right):

        if Left[i] <= Right[j]:
            returnArr.append(Left[i])
            i += 1
        else:
            returnArr.append(Right[j])
            j += 1

    while i < len(Left):
        returnArr.append(Left[i])
        i += 1

    while j < len(Right):
        returnArr.append(Right[j])
        j += 1

    return returnArr


def main(arr):

    print(merge_sort(arr))

if __name__ == '__main__':

    arr = [5,4,1,3,8,17,3,45,6,9,90]
    main(arr)

def findZeroSum(arr):
    # Write your code here.

    output = []
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        start = i + 1
        end = len(arr) - 1
        target = 0 - arr[i]

        while (start < end):

            if arr[start] + arr[end] == target:
                threesum_str = str(arr[start]) + ', ' + str(arr[end]) + ', ' + str(target * -1)
                output.append(threesum_str)

                while start + 1 < end and arr[start] == arr[start + 1]:
                    start += 1

                while end - 1 > start and arr[end] == arr[end - 1]:
                    end -= 1

                end -= 1
                start += 1

            elif arr[start] + arr[end] > target:
                end -= 1
            else:

                start += 1
    return output

def main(arr):

    print(findZeroSum(arr))

if __name__ == '__main__':

    arr = [10, 3, 3, 10,-4, -4, -6, 9]
    main(arr)
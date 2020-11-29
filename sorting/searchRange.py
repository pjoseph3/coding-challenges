def searchRange(nums, target):
    start = helper(nums, target, 0, len(nums)-1, True)
    end = helper(nums, target, 0, len(nums)-1, False)

    result = []

    result.append(start)
    result.append(end)

    return result


def helper(nums, target, start, end, isStart):
    returnIdx = -1
    while start <= end:

        mid = ((end + start) // 2)

        if isStart:
            if nums[mid] == target:
                returnIdx = mid

            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] == target:
                returnIdx = mid

            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1

    return returnIdx




def main(nums,target):

    print(searchRange(nums,target))


if __name__ == '__main__':
    nums = [5, 7, 7, 8]
    target = 7
    main(nums,target)
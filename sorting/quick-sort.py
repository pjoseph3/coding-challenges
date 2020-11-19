import random


def quick_sort(arr):
     helper(arr, 0, len(arr)-1)


def helper(arr, start, end):

    if start >= end:
        return

    pivotInt = random.randint(start, end)
    arr[pivotInt], arr[start] = arr[start], arr[pivotInt]

    high = start #bigger that pivot
    low = start #smaller than pivot

    pivot = arr[start]

    for high in range(start+1, end+1):

        if arr[high] <= pivot:
            low += 1
            arr[high], arr[low] = arr[low], arr[high]

    arr[low], arr[start] = arr[start], arr[low]

    helper(arr, start, low-1)
    helper(arr, low+1, end)





def main(arr):
    quick_sort(arr)
    print(arr)

if __name__ == '__main__':

    arr = [10,9,8,7,6,5,4,3,2,1,0]
    main(arr)
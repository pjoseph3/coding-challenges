def count_sort(arr,n):
    i=0

    for i in range(len(arr) - 1,-1,-1):
        if n < arr[i]:
           continue
        else:
            break

    arr.insert(i + 1, n)

    newArr = arr[1:]
    num = len(newArr)

    if num%2 == 0:
        return float((newArr[num//2]+newArr[num//2-1])/2)
    else:
        return newArr[num//2]







def main(arr,stream):
    arr.append(float('-inf'))
    for i in stream:
        print(count_sort(arr,i))

if __name__ == '__main__':

    arr = []
    stream = [1,0,3,5,2,0,1]
    main(arr,stream)
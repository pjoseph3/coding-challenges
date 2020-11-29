def sort_mat(mat):
    big_arr = []
    output = []
    for i in range(17):
        big_arr.append([])

    for start in range(0,len(mat[0]),4):
        new_list = dict()
        new_arr = []
        for i in range(len(mat)):
            list = []
            listj = 0
            for j in range(start,start+4):
                num = mat[i][j]
                list.append(num)
                if num == '?':
                    replace = (i,listj)
                else:
                    new_list.remove(int(num))
                listj += 1
            new_arr.append(list)
        replaced = new_list.pop()
        new_arr[replace[0]][replace[1]] = str(replaced)
        big_arr[replaced].append(new_arr)

    for i in range(4):
        list = []
        for arr in big_arr:
            if not arr:
                continue
            if len(arr) == 1:
                list+=arr[0][i]
            else:
                for arrays in arr:
                    list+=arrays[i]
        output.append(list)
    return output

def dict():
    new_list = set()
    for i in range(1,17):
        new_list.add(i)
    return new_list

def main(arr):
    print(sort_mat(arr))

if __name__ == '__main__':
    arr = [["1","2","3","4","1","2","3","4","1","16","3","4"],
           ["?","8","5","13","?","8","5","13","?","8","5","13"],
           ["6","7","9","16","6","7","9","10","6","7","9","15"],
           ["11","12","14","15","11","12","14","16","11","12","14","2"]]

    main(arr)

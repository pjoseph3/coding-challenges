global result


def find_all_arrangements(n):
    global result
    result = []
    grid = []
    for i in range(n):
        word = ""
        for j in range(n):
            word+="-"
        grid.append(word)
    helper(grid,n,0)
    return result


def helper(grid,n,row):
    global result

    if row == n:

        new_grid = []
        for i in range(n):
            word = ""
            for j in range(n):
                word += grid[i][j]
            new_grid.append(word)

        result.append(new_grid)
        return

    for i in range(n):

        if is_safe(grid,row,i):
            row_list = list(grid[row])
            row_list[i] = "q"
            grid[row]= "".join(row_list)

            helper(grid,n,row+1)

            row_list = list(grid[row])
            row_list[i] = "-"
            grid[row] = "".join(row_list)
    return


def is_safe(grid,row,col):

    i = 1

    while row - i >= 0:
        if grid[row - i][col] == 'q':
            return False
        i += 1

    i = 1
    while row - i >= 0 and col - i >= 0:
        if grid[row-i][col-i] == 'q':
            return False
        i +=1

    i = 1
    while row - i >= 0 and col + i < len(grid):
        if grid[row - i][col + i] == 'q':
            return False
        i += 1




    return True





def main(k):

    print(find_all_arrangements(k))


if __name__ == '__main__':
    main(5)
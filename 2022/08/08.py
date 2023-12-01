def main():
    with open("input.txt", "r") as f:
        file_input = f.read()
    file_input = file_input.split('\n')
    matrix = []
    for i in file_input:
        i = list(i)
        matrix.append(i)

    count_rows = 0
    count_columns = 0
    for i in range(len(matrix[0])):
        count_columns += 1
    for i in range(len(matrix)):
        count_rows += 1
    visible_edge = (count_rows+count_columns)*2-4

    counter_visible = 0
    for i in range(1, count_rows-1):
        for j in range(1, count_columns-1):
            is_visible = True
            for r in range(j+1, count_columns):
                if matrix[i][j] <= matrix[i][r]:
                    is_visible = False
                    break
            if is_visible == True:
                counter_visible += 1
                continue
            is_visible = True
            for r in range(0, j):
                if matrix[i][j] <= matrix[i][r]:
                    is_visible = False
                    break
            if is_visible == True:
                counter_visible += 1
                continue
            is_visible = True
            for r in range(i+1, count_rows):
                if matrix[i][j] <= matrix[r][j]:
                    is_visible = False
                    break                       
            if is_visible == True:
                counter_visible += 1
                continue
            is_visible = True
            for r in range(0, i):
                if matrix[i][j] <= matrix[r][j]:
                    is_visible = False
                    break
            if is_visible == True:
                counter_visible += 1  
                continue       
    print("Task1:", counter_visible+visible_edge)

    scenic_score = []
    for i in range(1, count_rows-1):
        for j in range(1, count_columns-1):
            c_right, c_left, c_up, c_down = 0, 0, 0, 0
            for r in range(j+1, count_columns):
                c_right += 1
                if matrix[i][j] <= matrix[i][r]:
                    break
            for r in reversed(range(0, j)):
                c_left += 1
                if matrix[i][j] <= matrix[i][r]:
                    break
            for r in range(i+1, count_rows):
                c_up += 1
                if matrix[i][j] <= matrix[r][j]:
                    break                       
            for r in reversed(range(0, i)):
                c_down += 1
                if matrix[i][j] <= matrix[r][j]:
                    break
            scenic_score.append(c_right*c_left*c_up*c_down)
    print("Task2:", max(scenic_score))
        

if __name__ == '__main__':
    main()


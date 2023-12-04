from pprint import pprint

def parsed_values(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data_into_list = data.split("\n")
    
    matrix = [list(line) for line in data_into_list] 
    matrix_result = [["." for i in range(len(matrix[0]))] for j in range(len(matrix))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not matrix[i][j].isalnum() and not matrix[i][j] == ".":
                line_up = max(0, i-1)
                line_down = min(len(matrix)-1, i+1)
                column_left = max(0, j-1)
                column_right = min(len(matrix[i])-1, j+1)
                for line in range(line_up, line_down+1):
                    for column in range(column_left, column_right+1):
                        if matrix[line][column].isdigit():
                            matrix_result[line][column] = matrix[line][column]
                            coursor = column
                            while coursor >=0 and matrix[line][coursor].isdigit():
                                matrix_result[line][coursor] = matrix[line][coursor]
                                coursor -= 1
                            coursor = column
                            while coursor < len(matrix) and matrix[line][coursor].isdigit():
                                matrix_result[line][coursor] = matrix[line][coursor]
                                coursor += 1

    result_list = []
    digit = ""
    for i in range(len(matrix_result)):
        for j in range(len(matrix_result[i])):
            if matrix_result[i][j].isdigit() and j < len(matrix_result[i]):
                digit += matrix_result[i][j]
                if j == len(matrix_result[i])-1:
                    result_list.append(int(digit))
                    digit = ""
            else:
                if digit != "":
                    result_list.append(int(digit))
                    digit = ""
    return sum(result_list)

def parsed_values_part2(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data_into_list = data.split("\n")
    
    matrix = [list(line) for line in data_into_list]
    
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "*":
                line_up = max(0, i-1)
                line_down = min(len(matrix)-1, i+1)
                column_left = max(0, j-1)
                column_right = min(len(matrix[i])-1, j+1)
                checked = []
                numbers = []
                for line in range(line_up, line_down+1):
                    for column in range(column_left, column_right+1):
                        if matrix[line][column].isdigit() and (line, column) not in checked:
                            digit = matrix[line][column]
                            checked.append((line, column))
                            coursor = column
                            while coursor >=0 and matrix[line][coursor].isdigit():
                                if (line, coursor) not in checked:
                                    digit = matrix[line][coursor] + digit
                                checked.append((line, coursor))
                                coursor -= 1
                            coursor = column
                            while coursor < len(matrix) and matrix[line][coursor].isdigit():
                                if (line, coursor) not in checked:
                                    digit += matrix[line][coursor]
                                checked.append((line, coursor))
                                coursor += 1
                            numbers.append(int(digit))
                if len(numbers) == 2:
                    sum += numbers[0] * numbers[1]
    return sum
    

def main():
    print("RESULT1: ", parsed_values("input.txt"))
    print("RESULT2: ", parsed_values_part2("input.txt"))
    

if __name__ == '__main__':
    main()


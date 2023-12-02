def parsed_values(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data_into_list = data.split("\n")

    result = []
    for i in data_into_list:
        result.append(calculate_color_amount(i))

    indexes = []

    for i in result:
        indexes.append(result.index(i) + 1)
        if any(j > 12 for j in i[0]) or any(j > 13 for j in i[1]) or any(j > 14 for j in i[2]):
            indexes.pop()
    return sum(indexes)

def parsed_values_part2(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data_into_list = data.split("\n")

    result = []
    for i in data_into_list:
        result.append(calculate_color_amount(i))

    biggest_numbers = []
    for i in result:
        a = []
        for j in i:
            a.append(max(j))
        biggest_numbers.append(a[0]*a[1]*a[2])

    return sum(biggest_numbers)    

def calculate_color_amount(line):
    line = line.replace(",", "")
    line = line.replace(";", "")
    line = line.split(" ")
    line = line[2:]

    red = []
    green = []
    blue = []
    rgb_sum = []
    for i in range(len(line)):
        if line[i] == "red":
            red.append(int(line[i-1]))
        elif line[i] == "green":
            green.append(int(line[i-1]))
        elif line[i] == "blue":
            blue.append(int(line[i-1]))
    rgb_sum.append(red)
    rgb_sum.append(green)
    rgb_sum.append(blue)
    return rgb_sum

def main():
    print("RESULT1: ", parsed_values("input.txt"))
    print("RESULT2: ", parsed_values_part2("input.txt"))
    

if __name__ == '__main__':
    main()


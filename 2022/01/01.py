def max_calories_sum(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data_into_list = data.split("\n\n")

    calorie_sums = []
    for x in data_into_list:
        x = x.split("\n")
        x = [int(i) for i in x]
        x = sum(x)
        calorie_sums.append(x)

    
    return max(calorie_sums)

def top3_calories_sum(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data = f.read()
    data_into_list = data.split("\n\n")

    calorie_sums = []
    for x in data_into_list:
        x = x.split("\n")
        x = [int(i) for i in x]
        x = sum(x)
        calorie_sums.append(x)
    
    top_3 = []
    top_3.append(max(calorie_sums))
    calorie_sums.remove(max(calorie_sums))
    top_3.append(max(calorie_sums))
    calorie_sums.remove(max(calorie_sums))
    top_3.append(max(calorie_sums))
    calorie_sums.remove(max(calorie_sums))
    return sum(top_3)


def main():
    print("Task1: ", max_calories_sum("input.txt"))
    print("Task2: ", top3_calories_sum("input.txt"))

if __name__ == '__main__':
    main()


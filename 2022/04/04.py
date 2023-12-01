def to_range(line):
    ranged_line = []
    for x in line:
        y = x.split("-")
        y = set(range(int(y[0]), int(y[1])+1, 1))
        ranged_line.append(y)
    return ranged_line

def is_contains(line_proc):  
    return line_proc[1].issubset(line_proc[0]) or line_proc[0].issubset(line_proc[1])

def is_overlap(line_proc):
    return line_proc[0] & line_proc[1]

def main():
    FILE = 'input.txt'
    with open(FILE, "r") as f:
        data = f.read()
    data_into_list = data.split("\n")

    count = 0
    for x in data_into_list:
        x = x.split(",")
        if is_contains(to_range(x)) == True:
            count += 1
    print("Task1:", count)

    count = 0
    for x in data_into_list:
        x = x.split(",")
        if is_overlap(to_range(x)) != set():
            count += 1
    print("Task2:", count)

if __name__ == '__main__':
    main()

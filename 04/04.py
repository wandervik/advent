def to_range(line):
    ranged_line = []
    for x in line:
        y = x.split("-")
        y = list(range(int(y[0]), int(y[1])+1, 1))
        ranged_line.append(y)
    return ranged_line

def pair_comparison(sections_ids):  
    line_proc = to_range(sections_ids)
    match = False
    if set(line_proc[1]).issubset(set(line_proc[0])) or set(line_proc[0]).issubset(set(line_proc[1])):
      match = True
    return match

def pair_overlap(sections_ids):
    line_proc = to_range(sections_ids)
    return (set(line_proc[0]) & set(line_proc[1]))

def main():
    FILE = 'input.txt'
    with open(FILE, "r") as f:
        data = f.read()
    data_into_list = data.split("\n")

    count = 0
    for x in data_into_list:
        x = x.split(",")
        if pair_comparison(x) == True:
            count += 1
    print("Task1:", count)

    count = 0
    for x in data_into_list:
        x = x.split(",")
        if pair_overlap(x) != set():
            count += 1
    print("Task2:", count)

if __name__ == '__main__':
    main()

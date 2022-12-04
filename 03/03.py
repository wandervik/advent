import string

def list_comparison(rucksack):
    rucksack_list = list(rucksack)
    length = len(rucksack_list)//2
    first_part, second_part = rucksack_list[:length], rucksack_list[length:] 
    items = list(string.ascii_letters)
    return items.index(next(iter((set(first_part) & set(second_part)))))+1

def three_list_comparison(rucksack_group):
    match = ''.join((set(list(rucksack_group[0])) & set(list(rucksack_group[1])) & set(list(rucksack_group[2]))))
    items = list(string.ascii_letters)
    return items.index(next(iter(match)))+1

def main():
    FILE = "input.txt"

    with open(FILE, "r") as f:
        data = f.read()
    data_into_list = data.split("\n")

    items_priorities = []
    for x in data_into_list:
        items_priorities.append(list_comparison(x))
    print("Task1:", sum(items_priorities))

    items_priorities = []
    for i in range(0, len(data_into_list), 3):
        items_priorities.append(three_list_comparison(data_into_list[i:i+3])) 
    print("Task2:", sum(items_priorities))

if __name__ == '__main__':
    main()

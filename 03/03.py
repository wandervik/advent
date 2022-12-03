import string

def list_comparison(rucksack):
    first_part = []
    second_part = []

    rucksack_list = list(rucksack)
    length = len(rucksack_list)//2

    for x in rucksack_list[:length]:
        first_part.append(x)

    for x in rucksack_list[length:]:
        second_part.append(x)

    # first_part, second_part = rucksack_list[:length], rucksack_list[length:] 

    match = (set(first_part) & set(second_part))
    items = list(string.ascii_letters)

    return items.index(next(iter(match)))+1

def three_list_comparison(rucksack_group):
    match = (set(list(rucksack_group[0])) & set(list(rucksack_group[1])) & set(list(rucksack_group[2])))
    match = ' '.join(match)
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
        x = i
        items_priorities.append(three_list_comparison(data_into_list[x:x+3])) 
    print("Task2:", sum(items_priorities))

if __name__ == '__main__':
    main()

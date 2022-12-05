COLUMNS_NUMBER = 9
RULES_FILE = "input-rules.txt"
STACK_FILE = "input-stack.txt"

def proccess_stacks(file):
    with open(file, "r") as f:
        stacks = f.read()
    stacks = stacks.split("\n")

    columns = []
    for i in range(COLUMNS_NUMBER):
        columns.append([])

    for stack in stacks:
        stack = stack[1::4]
        for (i, item) in enumerate(stack):
            if item != ' ' and not item.isdigit():
                columns[i].append(item)
    return columns

def proccess_rule(rule):
    proccessed_rule = []
    rule = rule.split(" ")
    for i in rule:
        if i.isdigit():
            proccessed_rule.append(i)
    return proccessed_rule

def rule_apply_fifo(rule, columns):
    items_count = int(rule[0])
    source_index = int(rule[1])-1
    dest_index = int(rule[2])-1

    for _ in range(items_count):
        popped_item = columns[source_index].pop(0)
        columns[dest_index].insert(0, popped_item)
    return columns

def rule_apply_ordered(rule, columns):
    items_count = int(rule[0])
    source_index = int(rule[1])-1
    dest_index = int(rule[2])-1

    popped_items = []
    for _ in range(items_count):
        popped_item = columns[source_index].pop(0)
        popped_items.append(popped_item)

    popped_items.reverse() 
    for i in popped_items:
        columns[dest_index].insert(0, i)

    return columns

def main():
    with open(RULES_FILE, "r") as f:
        rules = f.read()
    rules = rules.split("\n")

    rules_list = []
    for i in rules:
        rules_list.append(proccess_rule(i))

    stack = proccess_stacks(STACK_FILE)
    for i in rules_list:
        stack = rule_apply_fifo(i, stack)
    answer = ''
    for i in stack:
        answer += str(i[0])
    print('Task1:', answer)

    stack = proccess_stacks(STACK_FILE)
    for i in rules_list:
        stack = rule_apply_ordered(i, stack)
    answer = ''
    for i in stack:
        answer += str(i[0])
    print('Task2:', answer)

if __name__ == '__main__':
    main()


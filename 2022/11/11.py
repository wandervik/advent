def monkey_rules():
    with open("input.txt", "r") as f:
        file_input = f.read()
    monkeys = file_input.split('\n\n')

    monkeys_proc = []
    for i in monkeys:
        line = i.split('\n')
        items = []
        line[1] = line[1].split(' ')
        items = line[1][4:]
        items_proc = []
        for x in items:
            if x.endswith(','):
                x = x[:-1]
            items_proc.append(x)
        line[2] = line[2].split('= ')
        operation = line[2][1]
        line[3] = line[3].split(' ')
        test = line[3][5:]
        line[4] = line[4].split(' ')
        true_test = line[4][9:]
        line[5] = line[5].split(' ')
        false_test = line[5][9:]
        monkeys_proc.append([items_proc, operation, test[0], true_test[0], false_test[0]])
    return monkeys_proc

def monkey_test(item, operation, test):
    result = []
    old = item
    count = eval(operation)
    count = int(count / 3)
    result.append(count)
    result.append(count%test)
    return result

def monkey_test_2 (item, operation, test, mod):
    result = []
    old = item
    count = eval(operation)
    count = int(count)%mod
    result.append(count)
    result.append(count%test)
    return result

def main():
    monkeys_proc = monkey_rules()
    turn_counter = [0 for _ in range(len(monkeys_proc))]
    for _ in range(20):
        for mn, i in enumerate(monkeys_proc):
            while len(i[0]):
                turn_counter[mn] += 1
                x = i[0].pop(0)
                test = monkey_test(int(x), i[1], int(i[2]))
                if test[1] == 0:
                    monkeys_proc[int(i[3])][0].append(test[0])
                else:
                    monkeys_proc[int(i[4])][0].append(test[0])
    turn_counter.sort()
    turn_counter.reverse()
    print("Task1:", turn_counter[0]*turn_counter[1])

    monkeys_proc = monkey_rules()
    mod = 1
    for m in monkeys_proc:
        mod *= int(m[2])
    turn_counter = [0 for _ in range(len(monkeys_proc))]
    for h in range(10000):
        for mn, i in enumerate(monkeys_proc):
            while len(i[0]):
                turn_counter[mn] += 1
                x = i[0].pop(0)
                test = monkey_test_2(int(x), i[1], int(i[2]), mod)
                if test[1] == 0:
                    monkeys_proc[int(i[3])][0].append(test[0])
                else:
                    monkeys_proc[int(i[4])][0].append(test[0])
    turn_counter.sort()
    turn_counter.reverse()
    print("Task2:", turn_counter[0]*turn_counter[1])
    
if __name__ == '__main__':
    main()

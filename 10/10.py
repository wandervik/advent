def main():
    with open("input.txt", "r") as f:
        file_input = f.read()
    file_input = file_input.split('\n')

    file_input_proc = []
    for i in file_input:
        i = i.split(' ')
        if i[0].startswith('a'):
            file_input_proc.append(['addx','0'])
            file_input_proc.append(i)
        else:
            file_input_proc.append([i[0], 0])
    for i in file_input_proc:
        i[1] = int(i[1])

    x_value = 1
    cycle = 0
    result = []
    for i in file_input_proc:
        cycle += 1
        x_value += i[1]
        if cycle == 19 or cycle == 59 or cycle == 99 or cycle == 139 or cycle == 179 or cycle == 219:
            result.append(x_value*(cycle+1))
    print("Task1:", sum(result))

    x_value = 1
    crt_pos = 0
    print("Task2:")
    for i in file_input_proc:
        if abs(x_value - crt_pos) < 2:
            print('#', end='')
        else:
            print(' ', end='')
        crt_pos += 1
        x_value += i[1]
        if crt_pos == 40:
            crt_pos = 0
            print('')

if __name__ == '__main__':
    main()


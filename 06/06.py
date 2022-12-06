def find_element(code, chunks):
    for i in range(len(code)):
        x = code[:chunks]
        code.pop(0)
        if len(set(x)) == len(x):
            break
    return i+chunks

def main():
    with open("input.txt", "r") as f:
        file_input = f.read()
    print("Task1:", find_element(list(file_input), 4))
    print("Task2:", find_element(list(file_input), 14))

if __name__ == '__main__':
    main()


def main():
    with open("sample-input.txt", "r") as f:
        file_input = f.read()
    file_input = file_input.split('\n\n')
    
    for i in file_input:
        print(i)


    
if __name__ == '__main__':
    main()

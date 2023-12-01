def calibration_values(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data_into_list = data.split("\n")

    result = []
    for i in data_into_list:
        result.append(line_checker(i))
    
    return sum(result)
        


def line_checker(line):
    a = []
    for i in line:
        if i.isdigit():
            a.append(i)
    
    b = []
    b.append(a[0])
    b.append(a[-1])
    
    
    b = ''.join(b)
    return int(b)



def main():
    print("RESULT: ", calibration_values("input.txt"))
            

if __name__ == '__main__':
    main()


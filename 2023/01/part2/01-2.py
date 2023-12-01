def calibration_values(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data_into_list = data.split("\n")

    result = []
    for i in data_into_list:
        i = convert_word_to_numbers(i)
        result.append(line_checker(i))
    
    return sum(result)

def check_digit(line):
    word = ""
    for i in line:
        word = word+i
        if word == "one":
            line = line.replace("one", "1")
        elif word == "two":
            line = line.replace("two", "2")
        elif word == "three":
            line = line.replace("three", "3")
        elif word == "four":
            line = line.replace("four", "4")
        elif word == "five":
            line = line.replace("five", "5")
        elif word == "six":
            line = line.replace("six", "6")
        elif word == "seven":
            line = line.replace("seven", "7")
        elif word == "eight":
            line = line.replace("eight", "8")
        elif word == "nine":
            line = line.replace("nine", "9")       
    return line
        
def convert_word_to_numbers(line):
    a = []
    new_line = ""
    for i in range(len(line)):
        new_line=check_digit(line[i:])
        a.append(new_line)

    result = []
    for i in a:
        if i[0].isdigit():
            result.append(i[0])
            break


    for i in a[::-1]:
        if i[0].isdigit():
            result.append(i[0])
            break

    return result



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


def main():
    with open("data.txt", "r") as f:
        data = f.read()
    data_into_list = data.split("\n")
    result = []
    result = ''
    for i in data_into_list:
        y = i.split(" ")
        # result.append(y[4])
        result = result + y[4]
        result = result + ', '
    print(result)
        

    
    

    
if __name__ == '__main__':
    main()

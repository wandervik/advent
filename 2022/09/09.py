import math 
def sign(a):
    if a == 0:
        return 0
    else:
        return int(math.copysign(1, a))

def rope_two(input_steps):
    head = [0, 0]
    tail = [0, 0]
    counter = []
    for i in input_steps:
        for _ in range(int(i[1])):
            if i[0] == 'R':
                head[1] += 1
                if head[1] - tail[1] == 2:
                    tail[1] += 1
                    tail[0] = head[0]
            if i[0] == 'L':
                head[1] -= 1
                if head[1] - tail[1] == -2:
                    tail[1] -= 1
                    tail[0] = head[0]
            if i[0] == 'U':
                head[0] += 1
                if head[0] - tail[0] == 2:
                    tail[0] += 1
                    tail[1] = head[1]
            if i[0] == 'D':
                head[0] -= 1
                if head[0] - tail[0] == -2:
                    tail[0] -= 1
                    tail[1] = head[1]
            counter.append((tail[0], tail[1]))    
    return len(set(counter))

def rope_ten(input_steps):
    rope = []
    for r in range(10):
        rope.append([0, 0])
    # rope[ head (0): [0][0] . ...... . tail (9) [0][0]]

    counter = []
    for x in input_steps:
        for _ in range(int(x[1])):
            if x[0] == 'R':
                rope[0][1] += 1
            if x[0] == 'L':
                rope[0][1] -= 1              
            if x[0] == 'U':
                rope[0][0] += 1              
            if x[0] == 'D':
                rope[0][0] -= 1     
            for i in range(9):       
                if rope[i][1] - rope[i+1][1] == 2:
                    rope[i+1][1] += 1
                    rope[i+1][0] -= sign(rope[i+1][0] - rope[i][0])
                if rope[i][1] - rope[i+1][1] == -2:
                    rope[i+1][1] -= 1
                    rope[i+1][0] -= sign(rope[i+1][0] - rope[i][0])        
                if rope[i][0] - rope[i+1][0] == 2:
                    rope[i+1][0] += 1     
                    rope[i+1][1] -= sign(rope[i+1][1] - rope[i][1])
                if rope[i][0] - rope[i+1][0] == -2:
                    rope[i+1][0] -= 1
                    rope[i+1][1] -= sign(rope[i+1][1] - rope[i][1])
            counter.append((rope[9][0], rope[9][1]))
    return len(set(counter))
                                      
def main():
    with open("input.txt", "r") as f:
        file_input = f.read()
    file_input = file_input.split('\n')
    input_steps = []
    for i in file_input:
        i = i.split(' ')
        input_steps.append(i)
    print("Task1:", rope_two(input_steps))
    print("Task2:", rope_ten(input_steps))

if __name__ == '__main__':
    main()


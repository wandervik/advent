def next_character(ch):
    i = ord(ch)
    i = i + 1
    nch = chr(i)
    return nch

def recursive_search(step, current, end, signal_map, path):
    if current == end:
        return step
    if step > 1000:
        return 10001
    path.append(current)

    next_coords = []
    if current[1]+1 < len(signal_map[0]) and (path[current[0]][current[1]+1] == None or path[current[0]][current[1]+1] > step + 1) \
        and signal_map[current[0]][current[1]+1] <= next_character(signal_map[current[0]][current[1]]):
        next_coords.append([current[0], current[1]+1])

    if current[1]-1 >= 0 and (path[current[0]][current[1]-1] == None or path[current[0]][current[1]-1] > step + 1) \
        and signal_map[current[0]][current[1]-1] <= next_character(signal_map[current[0]][current[1]]):
        next_coords.append([current[0], current[1]-1])

    if current[0]+1 < len(signal_map) and (path[current[0]+1][current[1]] == None or path[current[0]+1][current[1]] > step + 1 ) \
        and signal_map[current[0]+1][current[1]] <= next_character(signal_map[current[0]][current[1]]):
        next_coords.append([current[0]+1, current[1]])

    if current[0]-1 >= 0 and (path[current[0]-1][current[1]] == None or path[current[0]-1][current[1]] > step + 1) \
        and signal_map[current[0]-1][current[1]] <= next_character(signal_map[current[0]][current[1]]):
        next_coords.append([current[0]-1, current[1]])
    
    results = [10000]
    for i in next_coords:
        path[i[0]][i[1]] = step+1
    for i in next_coords:
        results.append(recursive_search(step+1, i, end, signal_map, path))

    return min(results)

def main():
    with open("input.txt", "r") as f:
        file_input = f.read()
    file_input = file_input.split('\n')

    signal_map = []
    for i in file_input:
        signal_map.append(list(i))

    end_coord = []
    start_coord = []
    for i in range(len(signal_map)):
        for j in range(len(signal_map[0])):
            if signal_map[i][j] == 'E':
                end_coord = [i, j]
                signal_map[i][j] = 'z'
            if signal_map[i][j] == 'S':
                start_coord = [i, j]
                signal_map[i][j] = 'a'
    
    path_map = []
    for i in range(len(signal_map)):
        path_map.append([])
        for j in range(len(signal_map[0])):
            path_map[-1].append(None) 
    path_map[start_coord[0]][start_coord[1]] = 0

    print('Task1:', recursive_search(0, start_coord, end_coord, signal_map, path_map))

    a_list = []
    for i in range(len(signal_map)):
        for j in range(len(signal_map[0])):
            if signal_map[i][j] == 'a':
                a_list.append([i, j])

    results = []
    for a in a_list:
        results.append(recursive_search(0, a, end_coord, signal_map, path_map))
    print('Task2:', min(results))

    
if __name__ == '__main__':
    main()

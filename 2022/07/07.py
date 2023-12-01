def folder_size(data):
    content = []
    data = data.split('\n')
    for x in data:
        if x.startswith('dir'):
            content.append(x)
        elif x == '':
            continue
        elif x[0].isdigit():
            content.append(x)
    return content
    

def recursive(folders):
    folder_list = []
    for y in range(len(folders)):
        folder_content = folders[y][1]
        for f in folder_content:
            if f.startswith('dir'):
                dir = f
                dir = dir.replace('dir ', '')
                folder_content.remove(f)
                for x in folders:
                    if x[0] == dir:                        
                        for d in x[1]:
                            folder_content.append(d)
                        break
        folder_list.append([folders[y][0], folder_content])

    flat_list = [item for sublist in folder_list for item in sublist]
    flat_list = [item for sublist in flat_list for item in sublist]

    recursion_continue = ''
    for check in flat_list:
        if check.startswith('dir'):
            recursion_continue = True

    if recursion_continue:
        return recursive(folder_list)
    else:
        return folder_list

def distinct(data_input):
    data_input = data_input.split('\n')
    path = []
    out = []
    for line in data_input:
        items = line.strip().split()
        if items[1] == 'cd':
            if items[2] == '..':
                out.append(line)
                path.pop()
            else:
                path.append(items[2])
                out.append('$ cd ' + '/'.join(path))
        elif items[1] == 'ls':
            out.append(line)
        elif items[0] == 'dir':
            out.append('dir ' + '/'.join(path)+ '/' + items[1])
        else:
            out.append(line)
    return '\n'.join(out)


def main():
    with open("input.txt", "r") as f:
        file_input = f.read()
        
    file_input = distinct(file_input)
    with open("input-distict.txt", 'w') as f:
        f.write(file_input)

    file_input = file_input.split('$ ls')
    folders = []
    for i in range(len(file_input)):
        if file_input[i].startswith('$'):
            continue
        prev_element = file_input[i-1].split('\n')
        folder = prev_element[len(prev_element)-2]
        folder = folder.replace('$ cd ', '')
        folders.append([folder, folder_size(file_input[i])])
    folder_files = recursive(folders)

    folder_sizes_sums = []
    folder_sizes_sums_full = []
    folder_sizes_sums_goal = []

    full = 70000000
    free = 30000000

    system_size = 43956976
    delete_goal = free - (full - system_size)

    for i in range(len(folder_files)):
        folder_sizes = []
        files = folder_files[i]

        for f in files[1]:
            f = ''.join(x for x in f if x.isdigit())
            f = int(f)
            folder_sizes.append(f)
        if sum(folder_sizes) <= 100000:
            folder_sizes_sums.append([files[0], sum(folder_sizes)])
        if sum(folder_sizes):
            folder_sizes_sums_full.append([files[0], sum(folder_sizes)])
        if sum(folder_sizes) >= delete_goal:
            folder_sizes_sums_goal.append([files[0], sum(folder_sizes)])
    
    sizes = []
    for s in range(len(folder_sizes_sums)):
        size = folder_sizes_sums[s]
        sizes.append(size[1])
    print('Task1: ', sum(sizes))

    sizes_full = []
    for s in range(len(folder_sizes_sums_goal)):
        size = folder_sizes_sums_goal[s]
        sizes_full.append(size[1])
    print('Task2: ', min(sizes_full))

if __name__ == '__main__':
    main()
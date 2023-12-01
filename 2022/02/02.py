# X | A | Rock     | 1    Z .     0
# Y | B | Paper    | 2    Y       1  
# Z | C | Scissors | 3    X .     2

# Loose            | 0
# Draw             | 3
# Win              | 6

# Rock > Scissors > Paper > Rock
# X    > Z        > Y     > X

def game_score_actions(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data_into_list = data.split("\n")
    
    games_list=[]
    for x in data_into_list:
        x = x.split(" ")
        # print(x)
        games_list.append(x)

    game_result_list = []
    for x in games_list:
        # Rock > Scissors
        if x == ['A', 'Z']:
            game_result = 0 + 3
        # Rock < Paper
        elif x == ['A', 'Y']:
            game_result = 6 + 2
        # Rock = Rock
        elif x == ['A', 'X']:
            game_result = 3 + 1
        # Scissors > Paper
        elif x == ['C', 'Y']:
            game_result = 0 + 2
        # Scissors < Rock
        elif x == ['C', 'X']:
            game_result = 6 + 1
        # Scissors = Scissors
        elif x == ['C', 'Z']:
            game_result = 3 + 3
        # Paper > Rock
        elif x == ['B', 'X']:
            game_result = 0 + 1
        # Paper < Scissors
        elif x == ['B', 'Z']:
            game_result = 6 + 3
        # Paper = Paper
        elif x == ['B', 'Y']:
            game_result = 3 + 2
        game_result_list.append(game_result)
    return sum(game_result_list)
        

def game_score_result(file_name):

# X | Lose
# Y | Draw
# Z | Win

# A | Rock     
# B | Paper     
# C | Scissors  

    with open(file_name, "r") as f:
        data = f.read()
    data_into_list = data.split("\n")

    games_list=[]
    for x in data_into_list:
        x = x.split(" ")
        games_list.append(x)

    game_result_list = []
    for x in games_list:
        # Rock and Win = Paper
        if x == ['A', 'Z']:
            game_result = 6 + 2
        # Rock and Draw = Rock
        elif x == ['A', 'Y']:
            game_result = 3 + 1
        # Rock and Lose = Scissors
        elif x == ['A', 'X']:
            game_result = 0 + 3
        # Scissors and Draw = Scissors
        elif x == ['C', 'Y']:
            game_result = 3 + 3
        # Scissors and Lose = Paper
        elif x == ['C', 'X']:
            game_result = 0 + 2
        # Scissors and Win = Rock
        elif x == ['C', 'Z']:
            game_result = 6 + 1
        # Paper and Lose = Rock
        elif x == ['B', 'X']:
            game_result = 0 + 1
        # Paper and Win = Scissors
        elif x == ['B', 'Z']:
            game_result = 6 + 3
        # Paper and Draw = Paper
        elif x == ['B', 'Y']:
            game_result = 3 + 2
        game_result_list.append(game_result)
    return sum(game_result_list)

def main():
    # print("Task1:", game_score_actions("input-sample.txt"))
    # print("Task2:", game_score_result("input.txt"))

# X | A | Rock     | 1
# Y | B | Paper    | 2
# Z | C | Scissors | 3

# Loose            | 0
# Draw             | 3
# Win              | 6

# Rock > Scissors > Paper > Rock
# X    > Z        > Y     > X

    with open("input-sample.txt", "r") as f:
        data = f.read()
    data_into_list = data.split("\n")
    
    result = 0

    for line in data_into_list:
        games_list_elf, games_list_you = line.split()
        games_list_elf = "ABC".index(games_list_elf)
        games_list_you = "XYZ".index(games_list_you)
        result += games_list_you + 1
        match (games_list_you - games_list_elf) % 3:
            case 1:
                result += 6
            case 0:
                result += 3
    print(result)

if __name__ == '__main__':
    main()


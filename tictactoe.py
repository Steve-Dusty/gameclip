board = [
    ["0", "0", "0"],
    ["0", "0", "0"],
    ["0", "0", "0"]

]


def print_board():
    for y in board:
        print(y)


def move_to():
    while True:
        place = input("Send coordinates of where you want to move, split with comma: ").split(",")
        board[int(place[0])][int(place[1])] = "x"
        print_board()


print_board()
move_to()

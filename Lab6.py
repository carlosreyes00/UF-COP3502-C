
def initialize_board(num_rows, num_cols):
    board = []
    for i in range(num_rows):
        board.append(["-"] * num_cols)

    return board

def print_board(board):
    row_string = ""
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            row_string += board[i][j] + " "
        print(row_string[0:len(row_string)-1])
        row_string = ""

def insert_chip(board, col, chip_type):
    row = -1
    for i in range(len(board)):
        if board[i][col] == "-":
            board[i][col] = chip_type
            row = i
            break

    return row

def check_if_winner(board, col, row, chip_type):
    string_aux = ""

    # checking horizontal
    for i in range(0,len(board[0])):
        string_aux += board[row][i]

    # print(f"horizontal string_aux -> {string_aux}")
    if chip_type*4 in string_aux:
        # print(f"winner is {chip_type}")
        return True
    else:
        string_aux = ""

    # checking vertical
    for i in range(0,len(board)):
        string_aux += board[i][col]

    # print(f"vertical string_aux -> {string_aux}")
    if chip_type*4 in string_aux:
        # print(f"winner is {chip_type}")
        return True
    else:
        return False

def check_draw(board):
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j] == "-":
                return False

    return True


if __name__ == "__main__":
    height = int(input("What would you like the height of the board to be?"))
    length = int(input("What would you like the length of the board to be?"))

    board1 = initialize_board(height, length)
    print_board(board1)
    print()

    print("Player 1: x")
    print("Player 2: o\n")

    player1_is_playing = True

    while True:
        current_chip = 'x' if player1_is_playing else 'o'

        user_entry = int(input(f"Player {1 if player1_is_playing else 2}: Which column would you like to choose?"))
        row_inserted_in = insert_chip(board1, user_entry, current_chip)

        if check_if_winner(board1, user_entry, row_inserted_in, current_chip):
            print_board(board1)
            print()
            print(f"Player {1 if player1_is_playing else 2} won the game!")
            break
        elif check_draw(board1):
            print_board(board1)
            print()
            print('Draw. Nobody wins.')
            break

        player1_is_playing = not player1_is_playing
        print_board(board1)
        print()

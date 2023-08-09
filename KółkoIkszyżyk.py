def print_board(board):
    print("-------------")
    for row in range(3):
        print("|", end=" ")
        for col in range(3):
            print(board[row][col], "|", end=" ")
        print()
        print("-------------")

def check_win(board):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"
    moves = 0

    print("Witaj w grze KÓŁKO I KRZYŻYK!")
    print_board(board)
    while not check_win(board):
        print_board(board)
        if moves == 9:
            print("TO REMIS!")
            return play_game
        print(f"Gracz {current_player}, twoja kolej.")
        row = int(input("Wybierz wiersz (1-3): ")) - 1
        col = int(input("Wybierz kolumnę (1-3): ")) - 1
        if board[row][col] != " ":
            print("Już wybrałeś to pole. Spróbuj ponownie.")
        else:
            board[row][col] = current_player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
                moves += 1
            
    print(f"Gracz {current_player} WYGRYWA!")

play_game()

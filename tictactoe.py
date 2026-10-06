import math

board = [" "] * 9

def show_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])


def check_winner():
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "DRAW"

    return None


def minimax(is_max):
    result = check_winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "DRAW":
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best


def computer_move():
    best_score = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

    row = best_move // 3 + 1
    col = best_move % 3 + 1

    print("\nCOMPUTER MOVE")
    print("Computer placed O at Row", row, "Column", col)
    show_board()


def user_move():
    while True:
        row = int(input("\nEnter Row (1-3): "))
        col = int(input("Enter Column (1-3): "))

        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Invalid position!")
            continue

        position = (row - 1) * 3 + (col - 1)

        if board[position] != " ":
            print("Position already occupied!")
            continue

        board[position] = "X"

        print("\nYOUR MOVE")
        print("You placed X at Row", row, "Column", col)
        show_board()
        break




print("================================")
print("       TIC-TAC-TOE AI")
print("================================")
print("You = X")
print("Computer = O")

show_board()

while True:

    
    user_move()

    result = check_winner()

    if result == "X":
        print("\n************************")
        print("       YOU WIN!")
        print("************************")
        break

    if result == "DRAW":
        print("\n************************")
        print("       DRAW!")
        print("************************")
        break

  
    computer_move()

    result = check_winner()

    if result == "O":
        print("\n************************")
        print("    COMPUTER WINS!")
        print("************************")
        break

    if result == "DRAW":
        print("\n************************")
        print("       DRAW!")
        print("************************")
        break
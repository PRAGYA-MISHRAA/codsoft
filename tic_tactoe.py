board = [" "]*9

def show():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for line in wins:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
    return False

def ai():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            break

print("Tic-Tac-Toe. You = X, AI = O.")
show()

while True:
    move = int(input("Choose spot (1-9): ")) - 1
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Taken. Try again.")
        continue

    show()
    if check("X"):
        print("You win!")
        break
    if " " not in board:
        print("Draw!")
        break

    ai()
    show()
    if check("O"):
        print("AI wins!")
        break
    if " " not in board:
        print("Draw!")
        break

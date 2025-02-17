def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*5)
        
# board = [
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["X", " ", "O"]
# ]
# print_board(board)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
        
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0,1,2): "))
        col = int(input(f"Player {current_player}, enter row (0,1,2): "))
        
        if board[row][col] != " ":
            print("That position is already taken. Try again!")
            continue
            
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
            
        if is_board_full(board):
            print_board(board)
            print("Tie")
            break
            
        current_player = "0" if current_player == "X" else "X"
        
tic_tac_toe()
    

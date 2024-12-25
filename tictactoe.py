def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")


def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None


def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def main():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Get the player's move
        try:
            row = int(input(f"Player {player}, enter the row (0-2): "))
            col = int(input(f"Player {player}, enter the column (0-2): "))
            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Please enter valid numbers!")
            continue

        # Update the board
        board[row][col] = player
        print_board(board)

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break

        # Check for a draw
        if is_draw(board):
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    main()

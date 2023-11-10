# My assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.
# Here are the requirements:
#  2 players should be able to play the game (both sitting at the same computer)
#  The board should be printed out every time a player makes a move
#  You should be able to accept input of the player position and then place a symbol on the
# board.
# Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in
# Python" otherwise you won't learn anything!) Keep in mind that this project can take anywhere
# between several hours to several days.
# I encourage you to just try to start the project on your own without referencing any other source.
# There are parts of this that will be a struggle...and that is good! I have complete faith that if you
# have made it this far through the course you have all the tools and knowledge to tackle this
# project. Remember, it's totally open book, so take your time, do a little research, and remember:

# ------>>>>>>> Python code is here 

# Function to display the game board
def display_board(board):
    for row in board:
        # Print each row with pipes to separate columns
        print(" | ".join(row))
        # Add horizontal lines to separate rows
        print("-" * 9)

# Function to get input from players
def get_player_input(player):
    while True:
        try:
            # Get the row and column input from the player
            row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, or 2): "))
            
            # Check if the input is valid (within the board and the cell is empty)
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

# Function to check for a winner
def check_winner(board, player):
    for i in range(3):
        # Check if all cells in a row have the same player's symbol
        if all(board[i][j] == player for j in range(3)):
            return True
        # Check if all cells in a column have the same player's symbol
        if all(board[j][i] == player for j in range(3)):
            return True
    # Check if all cells in a diagonal have the same player's symbol
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    # If none of the above conditions are met, there is no winner
    return False

# Initialize the game board as a 3x3 grid with empty spaces
board = [[" " for _ in range(3)] for _ in range(3)]

# Main game loop
current_player = "X"

while True:
    display_board(board)  # Show the current state of the board
    row, col = get_player_input(current_player)  # Get input from the current player
    board[row][col] = current_player  # Place the player's symbol on the board

    # Check for a winner
    if check_winner(board, current_player):
        display_board(board)  # Display the final board
        print(f"Player {current_player} wins!")
        break  # Exit the loop

    # Check for a draw (all cells are filled)
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        display_board(board)  # Display the final board
        print("It's a draw!")
        break  # Exit the loop

    # Switch players for the next turn
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# ---->>>> c++ code here 

#include <iostream>
#include <vector>

using namespace std;

# // Function to display the game board
void displayBoard(const vector<vector<char>>& board) {
    for (const auto& row : board) {
        for (char cell : row) {
            cout << cell << " | ";
        }
        cout << endl << "---------" << endl;
    }
}

# // Function to check for a winner
bool checkWinner(const vector<vector<char>>& board, char player) {
    for (int i = 0; i < 3; ++i) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player) {
            return true; // Check rows
        }
        if (board[0][i] == player && board[1][i] == player && board[2][i] == player) {
            return true; // Check columns
        }
    }
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player) {
        return true; // Check diagonal from top-left to bottom-right
    }
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player) {
        return true; // Check diagonal from top-right to bottom-left
    }
    return false;
}

# // Function to check if the board is full (a draw)
bool isBoardFull(const vector<vector<char>>& board) {
    for (const auto& row : board) {
        for (char cell : row) {
            if (cell == ' ') {
                return false; // If there is an empty cell, the board is not full
            }
        }
    }
    return true; // All cells are filled, indicating a draw
}

int main() {
    vector<vector<char>> board(3, vector<char>(3, ' ')); // Initialize a 3x3 board with empty spaces
    char currentPlayer = 'X';

    while (true) {
        displayBoard(board);

        int row, col;
        cout << "Player " << currentPlayer << ", enter your move (row and column): ";
        cin >> row >> col;

        # // Check if the move is valid
        if (row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == ' ') {
            board[row][col] = currentPlayer;

            # // Check for a winner
            if (checkWinner(board, currentPlayer)) {
                displayBoard(board);
                cout << "Player " << currentPlayer << " wins!" << endl;
                break;
            }

            # // Check for a draw
            if (isBoardFull(board)) {
                displayBoard(board);
                cout << "It's a draw!" << endl;
                break;
            }

            # // Switch players
            currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
        } else {
            cout << "Invalid move. Try again." << endl;
        }
    }

    return 0;
}
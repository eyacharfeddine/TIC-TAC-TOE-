import math

class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9  # 3x3 board
        self.current_player = "X"  # Human always starts as "X"
        self.bot_player = "O"  # SmartBot's marker
        self.human_player = "X"  # Human's marker

    def print_board(self):
        """Display the game board."""
        print("\nCurrent Board:")
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---+---+---")
        print("\n")

    def is_winner(self, player):
        """Check if the given player has won."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6],             # Diagonals
        ]
        return any(all(self.board[pos] == player for pos in line) for line in win_conditions)

    def is_draw(self):
        """Check if the game is a draw."""
        return " " not in self.board

    def minimax(self, is_maximizing):
        """Minimax algorithm for SmartBot decision-making."""
        if self.is_winner(self.bot_player):
            return 1
        if self.is_winner(self.human_player):
            return -1
        if self.is_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = self.bot_player
                    score = self.minimax(False)
                    self.board[i] = " "
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = self.human_player
                    score = self.minimax(True)
                    self.board[i] = " "
                    best_score = min(best_score, score)
            return best_score

    def bot_move(self):
        """Determine SmartBot's best move."""
        print("SmartBot is analyzing the best possible move...")
        best_score = -math.inf
        best_move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.bot_player
                score = self.minimax(False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        print(f"SmartBot has chosen position {best_move + 1}.\n")
        return best_move

    def human_move(self):
        """Handle the human player's move."""
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move < 0 or move >= 9 or self.board[move] != " ":
                    raise ValueError
                print(f"You chose position {move + 1}.\n")
                return move
            except ValueError:
                print("Invalid move. Please choose an empty spot (1-9).")

    def play(self):
        """Main game loop."""
        print("Welcome to Tic-Tac-Toe!")
        print("You are X, and SmartBot is O. Try to win if you can!\n")
        self.print_board()

        while True:
            if self.current_player == self.human_player:
                print("Your turn!")
                move = self.human_move()
                self.board[move] = self.human_player
            else:
                print("SmartBot's turn!")
                move = self.bot_move()
                self.board[move] = self.bot_player

            self.print_board()

            # Check for a winner or draw
            if self.is_winner(self.current_player):
                if self.current_player == self.human_player:
                    print("Congratulations! You won! 🎉")
                else:
                    print(" SmartBot wins! Better luck next time!")
                break
            if self.is_draw():
                print("It's a draw! Well played!")
                break

            # Switch player
            self.current_player = (
                self.human_player if self.current_player == self.bot_player else self.bot_player
            )
        print("Game over! Thanks for playing.")

# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
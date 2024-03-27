class Board:
    """
    Represents a Sudoku board.

    Attributes:
        board (list): A 9x9 matrix representing the Sudoku board.
    """

    def __init__(self, board):
        """
        Initializes the Board with the given Sudoku board.

        Args:
            board (list): A 9x9 matrix representing the Sudoku board.
        """
        self.board = board

    def __str__(self):
        """
        Returns a string representation of the Sudoku board.

        Returns:
            str: The string representation of the Sudoku board.
        """
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines
        for index, line in enumerate(self.board):
            row_list = []
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                row_square = '|'.join(str(item) for item in part)
                row_list.extend(row_square)
                if square_no != 3:
                    row_list.append('║')

            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace('0', ' ')
            board_string += row_empty

            if index < 8:
                if index % 3 == 2:
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                else:
                    board_string += middle_lines
            else:
                board_string += lower_lines

        return board_string

    def find_empty_cell(self):
        """
        Finds the first empty cell (with value 0) in the Sudoku board.

        Returns:
            tuple or None: A tuple containing the row and column index of the empty cell,
                or None if no empty cell is found.
        """
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        """
        Checks if a number is valid to be placed in a row.

        Args:
            row (int): The row index.
            num (int): The number to be checked.

        Returns:
            bool: True if the number is valid in the row, False otherwise.
        """
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        """
        Checks if a number is valid to be placed in a column.

        Args:
            col (int): The column index.
            num (int): The number to be checked.

        Returns:
            bool: True if the number is valid in the column, False otherwise.
        """
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        """
        Checks if a number is valid to be placed in the 3x3 square.

        Args:
            row (int): The row index.
            col (int): The column index.
            num (int): The number to be checked.

        Returns:
            bool: True if the number is valid in the square, False otherwise.
        """
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        """
        Checks if placing a number in an empty cell is valid.

        Args:
            empty (tuple): A tuple containing the row and column index of the empty cell.
            num (int): The number to be placed.

        Returns:
            bool: True if placing the number in the empty cell is valid, False otherwise.
        """
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        """
        Solves the Sudoku puzzle using backtracking.

        Returns:
            bool: True if the puzzle is solvable, False otherwise.
        """
        if (next_empty := self.find_empty_cell()) is None:
            return True
        else:
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
        return False

def solve_sudoku(board):
    """
    Solves a Sudoku puzzle and prints the solved puzzle.

    Args:
        board (list): A 9x9 matrix representing the Sudoku puzzle.

    Returns:
        Board: A Board object representing the solved Sudoku puzzle.
    """
    # Create a Board object with the given Sudoku board
    gameboard = Board(board)
    # Print the original puzzle
    print(f'\nPuzzle to solve:\n{gameboard}')
    # Attempt to solve the Sudoku puzzle
    if gameboard.solver():
        # If the puzzle is solvable, print the solved puzzle
        print('\nSolved puzzle:')
        print(gameboard)
    else:
        # If the puzzle is unsolvable, print a message indicating that
        print('\nThe provided puzzle is unsolvable.')
    # Return the Board object representing the solved Sudoku puzzle
    return gameboard


# Example board to test below
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
# Example test
solve_sudoku(puzzle)  # Should give a solved board of Sudoku

class Sudoku:
    """a sudoku puzzle for the user to try and solver"""

    def __init__(self):
        """initializes variables"""
        self.game_board = [[None, 2, None, None, None, 4, 3, None, None],
                           [9, None, None, None, 2, None, None, None, 8],
                           [None, None, None, 6, None, 9, None, 5, None],
                           [None, None, None, None, None, None, None, None, 1],
                           [None, 7, 2, 5, None, 3, 6, 8, None],
                           [6, None, None, None, None, None, None, None, None],
                           [None, 8, None, 2, None, 5, None, None, None],
                           [1, None, None, None, 9, None, None, None, 3],
                           [None, None, 9, 8, None, None, None, 6, None]]


# each row in the square helper represents the coordinates of one sub 3x3 sub grid
square_helper = [[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
                 [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]],
                 [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]],
                 [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]],
                 [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]],
                 [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]],
                 [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]],
                 [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]],
                 [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]]


def print_board(board):
    """prints game board to terminal"""
    row_index = -1
    print("   0 1 2   3 4 5   6 7 8")
    print("   ---------------------")
    for row in board:
        row_index += 1
        if row_index % 3 == 0 and row_index != 0:
            # for legibility, separate the game squares
            print()
        to_print = ""
        column_index = -1
        for value in row:
            column_index += 1
            # for legibility, separate the game squares
            if column_index % 3 == 0 and column_index != 0:
                to_print += "  "
            if column_index == 0:
                to_print += str(row_index) + "| "
            if value is None:
                # if no value, put an x
                value = "X"
            to_print += str(value) + " "
        print(to_print)


def check_solution(board):
    """checks to users solution for correctness"""
    # check each row for an invalid solution
    for row_num in range(0, 9):
        # we are using a simplistic hash map style implementation for row, column,
        # and square value storing for constant time retrieval when checking for duplicates
        row_values = [None, None, None, None, None, None, None, None, None]
        for column_num in range(0, 9):
            value = board[row_num][column_num]
            # extra instance check here, in case of usage outside of CLI format
            if not isinstance(value, int) or value < 1 or value > 9 or row_values[value - 1] is not None:
                return "Not Solved Correctly... Game Over"
            else:
                row_values.append(value)

    # check each column for an invalid solution
    for column_num in range(0, 9):
        column_values = [None, None, None, None, None, None, None, None, None]
        for row_num in range(0, 9):
            value = board[row_num][column_num]
            if not isinstance(value, int) or value < 1 or value > 9 or column_values[value - 1] is not None:
                return "Not Solved Correctly... Game Over"
            else:
                column_values[value - 1] = value

    # check each "square" for a valid solution
    for square in square_helper:
        square_values = [None, None, None, None, None, None, None, None, None]
        for coord in square:
            # note that coord[0] represents the row and coord[1] represents the column of that coordinate
            value = board[coord[0]][coord[1]]
            if not isinstance(value, int) or value < 1 or value > 9 or square_values[value - 1] is not None:
                return "Not Solved Correctly... Game Over"
            else:
                square_values[value - 1] = value
    return "Solved Correctly! Congrats! Game Over"


if __name__ == '__main__':
    playing = True
    game = Sudoku()

    print("Welcome to CLI Sudoku!!! Each X on the grid represents an empty location that needs to be solved.")
    print("Remember the rules:")
    print("1. Each row must contain the numbers 1 - 9 with no repeated values")
    print("2. Each column must contain the numbers 1 - 9 with no repeated values")
    print("3. Each square must contain the numbers 1 - 9 with no repeated values")
    print()
    print(" Have fun :D")
    print()
    print("Make your move by inputting a row and column coordinate, then enter a value to place there.")
    print()

    # for testing, modify as you see fit!
    """game.game_board =     [[8, 2, 7, 1, 5, 4, 3, 9, 6],
                           [9, 6, 5, 3, 2, 7, 1, 4, 8],
                           [3, 4, 1, 6, 8, 9, 7, 5, 2],
                           [5, 9, 3, 4, 6, 8, 2, 7, 1],
                           [4, 7, 2, 5, 1, 3, 6, 8, 9],
                           [6, 1, 8, 9, 7, 2, 4, 3, 5],
                           [7, 8, 6, 2, 3, 5, 9, 1, 4],
                           [1, 5, 4, 7, 9, 6, 8, 2, 3],
                           [2, 3, 9, 8, 4, 1, 5, 6, 7]]"""
    # game loop begins here
    while playing:
        print_board(game.game_board)
        print()
        row_number = input("select row number: ")
        column_number = input("select column number: ")
        coord_error = False

        # we check here for valid input
        try:
            row_number = int(row_number)
            column_number = int(column_number)
        except ValueError:
            coord_error = True

        if coord_error or column_number < 0 or column_number > 8 or row_number < 0 or row_number > 8:
            print()
            print("invalid input")
            print()
        else:
            value_error = False
            value = input("value to input: ")

            # we check here for valid input
            try:
                value = int(value)
            except ValueError:
                print()
                print("invalid input")
                print()
                value_error = True

            if not value_error:
                game.game_board[row_number][column_number] = value
                print()
        # check end condition, by searching for a complete puzzle
        for row in game.game_board:
            if None in row:
                playing = True
                break
            else:
                playing = False
    print("checking solution...")
    print(check_solution(game.game_board))

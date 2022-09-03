import random
from basic import Sudoku


class SudokuGenerator:
    def __init__(self):
        self.board = [[0 for j in range(9)] for i in range(9)]

    def solve(self):
        row, col = Sudoku.find_empty(self)
        if row is None:
            return True
        pos_val = Sudoku.guess(self, row, col)
        if row == 0 and col == 0:
            r = random.randint(0, 8)
            c = random.randint(0, 8)
            v = random.choice(pos_val)
            self.board[r][c] = v
            # print(r, c, v)
        for i in pos_val:
            self.board[row][col] = i
            if self.solve():
                return True
        self.board[row][col] = 0
        return False

    def obscure(self):
        obscured_val = random.randint(46, 64)
        # print(obscured_val)
        for i in range(obscured_val):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while self.board[row][col] == 0:
                row = random.randint(1, 8)
                col = random.randint(1, 8)
            self.board[row][col] = 0
        return self.board


if __name__ == "__main__":
    obj = SudokuGenerator()
    obj.solve()
    board = obj.obscure()
    b = Sudoku(board)
    b.display()
    b.solve()
    b.display()

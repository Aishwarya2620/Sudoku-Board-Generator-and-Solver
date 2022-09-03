import pprint
import random


class Sudoku:
    def __init__(self, board):
        self.board = board

    def display(self):
        pprint.pprint(self.board)

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return None, None

    def guess(self, row, col):
        pos_val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        c_val = [self.board[i][col] for i in range(9)]
        for i in self.board[row]:
            if i in pos_val:
                pos_val.remove(i)
        for i in c_val:
            if i in pos_val:
                pos_val.remove(i)
        r_s = (row // 3) * 3
        c_s = (col // 3) * 3
        for r in range(r_s, r_s + 3):
            for c in range(c_s, c_s + 3):
                if self.board[r][c] in pos_val:
                    pos_val.remove(self.board[r][c])
        return pos_val

    def solve(self):
        row, col = self.find_empty()
        if row is None:
            return True
        pos_val = self.guess(row, col)
        for i in pos_val:
            self.board[row][col] = i
            if self.solve():
                return True
        self.board[row][col] = 0
        return False


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

    def solved_board(self):
        self.solve()
        return self.board


if __name__ == "__main__":
    print("YOUR NEW SUDOKU CHALLENGE IS:")
    obj = SudokuGenerator()
    obj.solve()
    grid = obj.obscure()
    obj1 = Sudoku(grid)
    obj1.display()
    print("YOUR SOLUTION IS:")
    obj1.solve()
    obj1.display()
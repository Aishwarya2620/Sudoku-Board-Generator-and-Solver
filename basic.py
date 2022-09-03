import pprint


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


obj = Sudoku([[1, 4, 2, 0, 0, 6, 7, 8, 0],
              [3, 5, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 4, 0, 5, 6],
              [0, 0, 0, 0, 0, 5, 0, 0, 7],
              [4, 6, 0, 8, 0, 7, 0, 0, 0],
              [0, 9, 0, 2, 0, 3, 0, 0, 0],
              [5, 2, 0, 0, 3, 0, 0, 0, 0],
              [6, 0, 1, 0, 7, 8, 0, 0, 0],
              [9, 0, 0, 5, 0, 0, 0, 0, 0]])
if __name__ == "__main__":
    # obj = Sudoku([[0, 0, 7, 5, 8, 6, 2, 3, 1],
    #               [8, 0, 0, 9, 2, 7, 5, 0, 0],
    #               [0, 6, 0, 3, 0, 0, 9, 0, 0],
    #               [0, 7, 5, 4, 6, 1, 8, 2, 3],
    #               [0, 8, 6, 2, 0, 5, 4, 7, 9],
    #               [3, 2, 4, 8, 7, 9, 0, 1, 0],
    #               [0, 0, 0, 6, 5, 2, 1, 9, 8],
    #               [0, 0, 0, 1, 9, 0, 7, 0, 4],
    #               [6, 0, 9, 7, 0, 0, 0, 0, 0]])

    obj.display()
    obj.solve()
    print("*" * 120)
    obj.display()

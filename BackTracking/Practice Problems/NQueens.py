from typing import List


class NQueens:

    def queens(self, Board: List[List[bool]], row: int):
        if row == len(Board):
            self.display(Board)
            print()
            return 1

        count: int = 0

        # placing rhe queen and checking for every row and column
        for col in range(len(Board)):
            # place the queen if it is safe
            if self.isSafe(Board, row, col):
                Board[row][col] = True
                count += self.queens(Board, row + 1)
                Board[row][col] = False

        return count

    def isSafe(self, Board, row, col):
        # check vertical row
        for i in range(row):
            if Board[i][col]:
                return False

        # diagonal left
        max_left = min(row,col)
        for i in range(1, max_left + 1):
            if Board[row - i][col - i]:
                return False

        # diagonal right
        max_right = min(row,  len(Board) - col - 1)
        for i in range(1, max_right + 1):
            if Board[row - i][col + i]:
                return False

        return True

    def display(self, Board: List[List[bool]]):
        for row in Board:
            for element in row:
                if element:
                    print('Q', end='')
                else:
                    print('.', end='')

            print()


if __name__ == '__main__':
    n: int = 4
    board: List[List[bool]] = [[False for _ in range(n)] for _ in range(n)]

    NQueens().queens(board, 0)

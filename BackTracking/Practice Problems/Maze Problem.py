"""

given a 3X3 matrix,
walk only right or down,
no of ways to reach last

ans: RRDD, DDRR, RDDR, DRDR

"""


class Maze:
    def count(self, r, c):
        if r == 1 or c == 1:
            return 1

        left = self.count(r - 1, c)
        right = self.count(r, c - 1)

        return left + right


if __name__ == '__main__':
    print(Maze().count(4, 4))

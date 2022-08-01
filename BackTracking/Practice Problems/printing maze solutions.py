"""

given a 3X3 matrix,
walk only right or down,
no of ways to reach last

ans: RRDD, DDRR, RDDR, DRDR

"""


class Maze:

    def __init__(self):
        self.path_list = []

    def count(self, path, r, c):
        if r == 1 and c == 1:
            self.path_list.append(path)
            return

        if r > 1:
            self.count(path + 'D', r - 1, c)

        if c > 1:
            self.count(path + 'R', r, c - 1)

        return self.path_list


if __name__ == '__main__':
    print(Maze().count("", 3, 3))

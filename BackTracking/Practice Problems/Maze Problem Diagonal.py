"""

given a 3X3 matrix,
walk only right, down or diagonal,
no of ways to reach last

"""


class Maze:

    def __init__(self):
        self.path_list = []

    def count(self, path, r, c):
        if r == 1 and c == 1:
            self.path_list.append(path)
            return

        if r > 1 and c > 1:
            self.count(path + 'D', r - 1, c - 1)

        if r > 1:
            self.count(path + 'V', r - 1, c)

        if c > 1:
            self.count(path + 'H', r, c - 1)

        return self.path_list


if __name__ == '__main__':
    print(Maze().count("", 4, 4))

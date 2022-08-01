"""

given a 3X3 matrix,
walk only right or down,
no of ways to reach last
there are obstacles in the path

"""


class Maze:

    def __init__(self):
        self.path_list = []

    def pathObstacles(self, path, maze, r, c):
        if r == len(maze) - 1 and c == len(maze[0]) - 1:
            print(path)
            return

        if not maze[r][c]:
            return

        # I am considering this block in my path
        maze[r][c] = False

        if r < len(maze) - 1:
            self.pathObstacles(path + 'D', maze, r + 1, c)

        if c < len(maze[0]) - 1:
            self.pathObstacles(path + 'R', maze, r, c + 1)

        if r > 0:
            self.pathObstacles(path + 'U', maze, r - 1, c)

        if c > 0:
            self.pathObstacles(path + 'U', maze, r, c - 1)

        # This line is where the function will be over
        # so before the function is removed, remove the changes that were made by that function
        maze[r][c] = True


if __name__ == '__main__':

    maze_bool = [[True, True, True], [True, True, True], [True, True, True]]
    (Maze().pathObstacles("", maze_bool, 0, 0))

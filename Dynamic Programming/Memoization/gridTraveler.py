# 2D grid, begin from top left corner to the bottom right corner, move only to down or right
# How many ways can you travel from top left corner to the bottom right corner

class GridTraveler:
    def grid(self, m: int, n: int, memo=None) -> int:
        if memo is None:
            memo = {}
        key = str(m) + ',' + str(n)

        if key in memo:
            return memo[key]

        if m == 1 and n == 1:
            return 1

        if m == 0 or n == 0:
            return 0

        memo[key] = self.grid(m - 1, n, memo) + self.grid(m, n - 1, memo)
        return memo[key]


if __name__ == '__main__':
    print(GridTraveler().grid(1, 1))
    print(GridTraveler().grid(2, 3))
    print(GridTraveler().grid(3, 2))
    print(GridTraveler().grid(3, 3))
    print(GridTraveler().grid(18, 18))
    print(GridTraveler().grid(32, 32))
    print(GridTraveler().grid(64, 64))
    print(GridTraveler().grid(128, 128))
    print(GridTraveler().grid(256, 256))

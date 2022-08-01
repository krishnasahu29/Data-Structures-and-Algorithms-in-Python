# Sunny Number is a number where square root of (n + 1) is an integer
import math


class Sunny:

    def number(self, n):
        return (math.sqrt(n + 1)) % 1 == 0


if __name__ == '__main__':
    print(Sunny().number(245))

# A number is said to be magic when the recursive sum of the digits is 1
# For e.g. number 50311, 5 + 0 + 3 + 1 + 1 = 10 = 1

class Magic:

    def __init__(self):
        self.set = set()

    def number(self, n):
        if n == 1:
            return True

        s = 0

        while n > 0:
            s += n % 10
            n = n // 10

        print(s)

        if s in self.set:
            return False

        else:
            self.set.add(s)

        return self.number(s)


if __name__ == '__main__':
    print(Magic().number(119))

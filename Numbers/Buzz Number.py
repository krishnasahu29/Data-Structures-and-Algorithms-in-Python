# Buzz no is divisble by 7 or ends with 7

class Buzz:
    def number(self, n):
        return n % 7 == 0 or n % 10 == 7


if __name__ == '__main__':
    print(Buzz().number(10))

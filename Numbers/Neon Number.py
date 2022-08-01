# Neon number where the sum of digits of square of a number is equal to the number

class Neon:

    def number(self, n):
        m = n ** 2

        s = 0
        while m > 0:
            s += m % 10
            m = m // 10

        return s == n


if __name__ == '__main__':
    print(Neon().number(10))
    
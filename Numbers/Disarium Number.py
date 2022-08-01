# Disarium Number is a number where sum of its digits powered with
# their respective position is equal to the number

class Disarium:

    def number(self, n):
        i = len(str(n))
        s = 0
        m = n

        while n > 0:
            r = n % 10
            s += r ** i

            i -= 1
            n //= 10

        return s == m


if __name__ == '__main__':
    print(Disarium().number(58))

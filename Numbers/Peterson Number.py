# Peterson Number is sum of factorial of each digit = number

class Peterson:

    def number(self, n):

        s = 0
        m = n
        while n > 0:
            r = n % 10
            s += self.factorial(r)

            n //= 10

        return s == m

    def factorial(self, n):
        if n == 1 or n == 0:
            return 1

        else:
            return n * self.factorial(n - 1)


if __name__ == '__main__':
    print(Peterson().number(145))

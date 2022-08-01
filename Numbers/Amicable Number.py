class Amicable:

    def number(self, a, b):
        return self.sum_divisors(a) == b

    def sum_divisors(self, n):
        i = 1
        s = 0

        while i < n:
            if n % i == 0:
                s += i

            i += 1

        return s

if __name__ == '__main__':
    print(Amicable().number(17296, 18416))

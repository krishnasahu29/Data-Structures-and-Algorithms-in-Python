def calculateSumOfPrime(inputArray):
    s = 0
    for num in inputArray:
        if check_prime(num):
            s += num

    return s

def check_prime(n):
    c = 0
    i = 2
    while i <= n:
        if n % i == 0:
            c += 1

        i += 1

    return c == 1


if __name__ == '__main__':
    print(calculateSumOfPrime([619, 514, 857, 518, 825, 940, 585]))

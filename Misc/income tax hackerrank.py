def slab(income):

    amt = 0
    if 0 < income <= 250000:
        amt = income

    elif 250000 < income <= 500000:
        amt = 0.05 * income + income

    elif 500000 < income <= 750000:
        amt = 0.1 * income + income

    elif 750000 < income <= 1000000:
        amt = 0.15 * income + income

    elif 1000000 < income <= 1250000:
        amt = 0.2 * income + income

    elif 1250000 < income <= 1500000:
        amt = 0.25 * income + income

    else:
        amt = 0.3 * income + income

    return amt

def calcIncomeTax(income):
    amt = 0

    income_tax = slab(income)
    amt = surcharge(income_tax, income)

    amt += 0.04 * income_tax + income

    return amt

def surcharge(income_tax, income):

    amt = 0

    if 5000000 < income <= 10000000:
        amt = 0.1 * income_tax + income

    elif 10000000 < income <= 20000000:
        amt = 0.15 * income_tax + income

    elif 20000000 < income <= 50000000:
        amt = 0.25 * income_tax + income

    elif income > 50000000:
        amt = 0.1 * income_tax + income

    return amt


if __name__ == '__main__':
    print(calcIncomeTax(1500000))

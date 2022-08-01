weights = [2, 4, 6, 6, 4, 2, 4]
c = 0

hash_table = {}

for item in weights:
    if item in hash_table.keys():
        hash_table[item] += 1

    else:
        hash_table[item] = 1

for i in hash_table.keys():
    dev = hash_table[i] // 3
    rem = hash_table[i] % 3

    c += dev
    if rem == 2:
        c += 1

print(c)

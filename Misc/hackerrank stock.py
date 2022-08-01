from itertools import permutations, combinations

lists = [1, 2, 7, 7, 4, 3, 6]
k = 3
perm = combinations(lists, k)
res = []
maxi = 0

for item in perm:
    if len(set(item)) != len(item):
        continue

    else:
        res.append(item)

for item in res:
    if sum(item) > maxi:
        maxi = sum(item)

print(maxi)

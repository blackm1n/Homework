lst = [1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6]
res = [item for item in set(lst) if lst.count(item) > 1]
print(res)
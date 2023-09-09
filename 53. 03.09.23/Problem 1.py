items = {"friend1": ("item1", "item2", "item3"), "friend2": ("item1", "item2", "item4"), "friend3": ("item2", "item3")}

values = list(items.values())

set1 = set(values[0])
for v in values[1:]:
    set1 = set1.intersection(set(v))

print(set1)

set2 = set()
for v1 in values:
    v1set = set(v1)
    for v2 in values:
        if v1 != v2:
            v1set = v1set.difference(set(v2))
    set2 = set2.union(v1set)

print(set2)

res3 = []
for k1, v1 in items.items():
    v1set = set(v1)
    lst = []
    for k2, v2 in items.items():
        if v1 != v2:
            lst.append(set(v2).difference(v1set))
    diff_set = lst[0]
    for s in lst:
        diff_set = diff_set.intersection(s)
    if len(diff_set) > 0:
        for i in diff_set:
            res3.append((k1, i))

print(res3)
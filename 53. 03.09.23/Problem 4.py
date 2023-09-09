backpack = {"item1": 1, "item2": 2, "item3": 3, "item4": 4}
max_load = 5


def backpack_variation(backpack: dict, max_load: int):
    res = [[]]
    for k, v in backpack.copy().items():
        backpack.pop(k)
        if v <= max_load:
            rec_res = backpack_variation(backpack.copy(), max_load - v)
            for lst in rec_res:
                lst.append(k)
            res += rec_res
    return res


print(backpack_variation(backpack, max_load))

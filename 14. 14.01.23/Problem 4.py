# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def RLE_Compress(string):
    count = 0
    result = []
    for i in range(len(string)):
        count += 1
        if i < len(string) - 1:
            if string[i] != string[i + 1]:
                result.append([count, string[i]])
                count = 0
        else:
            result.append([count, string[i]])

    count = 0
    inserted = 0
    memory = ""
    for i in range(len(result)):
        i += inserted
        if result[i][0] == 1:
            count += 1
            memory += result[i][1]
        else:
            if len(memory) > 1:
                result.insert(i, [-count, memory])
                inserted += 1
                count = 0
                memory = ""
        if i == len(result) - 1 and len(memory) > 1:
            result.append([-count, memory])

    popped = 0
    for i in range(len(result) - 1):
        if result[i - popped][0] == 1 and (result[i - popped + 1][0] == 1 or result[i - popped + 1][0] < 0):
            result.pop(i - popped)
            popped += 1
    return result


def RLE_Uncompress(RLE):
    result = ""
    for i in range(len(RLE)):
        if RLE[i][0] > 0:
            result += RLE[i][1] * RLE[i][0]
        else:
            result += RLE[i][1]
    return result


string = input("Введите строку: ")

compressed = RLE_Compress(string)

print(compressed)

print(RLE_Uncompress(compressed))

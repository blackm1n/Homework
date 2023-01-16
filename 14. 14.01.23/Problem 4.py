# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def RLE_Compress(string):
    count = 0
    result = []
    j = 0
    state = 0
    for i in range(len(string)):
        print(result)
        if state == 0:
            count = 1
            result.append([count, string[i]])
            if i < len(string) - 1:
                if string[i] == string[i + 1]:
                    state = 1
                else:
                    state = 2
            continue
        elif state == 1:
            count += 1
            result[j][0] = count
            if i < len(string) - 1:
                if string[i] != string[i + 1]:
                    state = 0
                    j += 1
        elif state == 2:
            if i < len(string) - 1:
                if string[i] == string[i + 1]:
                    state = 1
                    j += 1
                    count = 1
                    result.append([count, string[i]])
                    if i < len(string) - 1:
                        if string[i] == string[i + 1]:
                            state = 1
                        else:
                            state = 2
                    continue
            count += 1
            result[j][0] = -count
            result[j][1] += string[i]
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

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def RLE_Compress(string):
    count = 0
    RLE = []
    j = 0
    state = 0
    for i in range(len(string)):
        if state == 0:
            count = 1
            RLE += ([str(count), string[i]])
            if i < len(string) - 1:
                if string[i] == string[i + 1]:
                    state = 1
                else:
                    state = 2
            continue
        elif state == 1:
            count += 1
            RLE[j * 2] = str(count)
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
                    RLE += ([str(count), string[i]])
                    if i < len(string) - 1:
                        if string[i] == string[i + 1]:
                            state = 1
                        else:
                            state = 2
                    continue
            count += 1
            RLE[j * 2] = str(-count)
            RLE[j * 2 + 1] += string[i]
    result = "".join(RLE)
    return result

def RLE_Uncompress(string):
    num = ""
    skip = 0
    result = ""
    for i in range(len(string)):
        if string[i].isdigit() and skip > 0:
            continue
        elif string[i].isdigit():
            num += string[i]
        elif string[i].isalpha() and skip > 0:
            result += string[i]
            skip -= 1
        elif string[i].isalpha():
            result += string[i] * int(num)
            num = ""
        elif string[i] == "-":
            if string[i + 1].isdigit():
                skip = int(string[i + 1])
    return result
def ApplyFunctionToFile(function, input_file, output_file):
    with open(input_file, 'r') as file_i:
        with open(output_file, 'w') as file_o:
            file_o.write(function(file_i.read()))

ApplyFunctionToFile(RLE_Compress, 'file_initial.txt', 'file_compressed.txt')
ApplyFunctionToFile(RLE_Uncompress, 'file_compressed.txt', 'file_uncompressed.txt')
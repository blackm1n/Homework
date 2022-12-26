# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# Данное решение связано с четвортой задачей. Я не знаю, что я делал, но в конце концов оно работает. А это самое главное.

def tryint(string):
    if string == '':
        return 1
    else:
        return int(string)


with open('file1.txt', 'r') as file:
    file1 = list(map(str, file.read().split('+')))
with open('file2.txt', 'r') as file:
    file2 = list(map(str, file.read().split('+')))

polynomial = []
for i in file1:
    polynomial.append(i)
for i in file2:
    polynomial.append(i)

maxexp = 0
for i in polynomial:
    if "^" in i:
        if int(i[i.index("^") + 1:]) > maxexp:
            maxexp = int(i[i.index("^") + 1:])

result = []
breaked = False
for exp in range(-maxexp, 1):
    exp = -exp
    for i in range(len(polynomial)):
        if breaked == True:
            breaked = False
            break
        for j in range(i + 1, len(polynomial)):
            if exp > 1:
                if "^" in polynomial[i] and "^" in polynomial[j]:
                    if polynomial[i][polynomial[i].index("^"):] == polynomial[j][polynomial[j].index("^"):] == f'^{exp}':
                        result.append(f'{tryint(polynomial[i][:polynomial[i].index("x")]) + tryint(polynomial[j][:polynomial[j].index("x")])}x^{exp}')
                        polynomial.pop(i)
                        polynomial.pop(j - 1)
                        breaked = True
                        break
                elif "^" in polynomial[i]:
                    if polynomial[i][polynomial[i].index("^"):] == f'^{exp}' and j == len(polynomial) - 1:
                        result.append(f'{tryint(polynomial[i][:polynomial[i].index("x")])}x^{exp}')
                        polynomial.pop(i)
                        breaked = True
                        break
            elif exp == 1:
                if "x" in polynomial[i] and "x" in polynomial[j]:
                    result.append(f'{tryint(polynomial[i][:polynomial[i].index("x")]) + tryint(polynomial[j][:polynomial[j].index("x")])}x')
                    polynomial.pop(i)
                    polynomial.pop(j - 1)
                    breaked = True
                    break
                elif "x" in polynomial[i] and j == len(polynomial) - 1:
                    result.append(f'{tryint(polynomial[i][:polynomial[i].index("x")])}x')
                    polynomial.pop(i)
                    breaked = True
                    break
            else:
                result.append(f'{int(polynomial[i]) + int(polynomial[j])}')
        if len(polynomial) == 1 and exp == 0:
            result.append(f'{int(polynomial[0])}')

print(result)

with open('file3.txt', 'a') as file:
    for i in range(len(result)):
        if i < len(result) - 1:
            file.write(f'{result[i].replace("1x", "x")}+')
        else:
            file.write(f'{result[i]}')

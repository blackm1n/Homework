from sys import argv
from package import *

if len(argv) > 1:
    date = argv[1]
else:
    date = input("Введите дату в виде DD.MM.YYYY: ")

print(date_check(date))

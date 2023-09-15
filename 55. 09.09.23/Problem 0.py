# Говорили join'ы, join'ы, да одни лишь join'ы? Представляю вам решение без join'оф.

print(*(f'{i + (k * 4)} * {j} = {(i + (k * 4)) * j}' + "\t" if i != 6 else "\n" if j != 10 else "\n\n" for k in range(2) for j in range(2, 11) for i in range(2, 7)), sep="")
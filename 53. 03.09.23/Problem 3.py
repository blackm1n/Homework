with open('lorem ipsum.txt', 'r') as file:
    text = file.readlines()

word_count = {}
for line in text:
    line = line.lower().replace(".", "").replace(",", "").replace(";", "").replace("\n", "")
    words = line.split()
    for word in words:
        word_count.setdefault(word, 0)
        word_count[word] += 1

word_list = sorted(word_count.items(), key=lambda word: word[1], reverse = True)
for i in range(10):
    print(word_list[i])
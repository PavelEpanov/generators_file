def find_word(f, word):
    global_index = 0
    for line in f:
        index = 0
        while index != -1:
            index = line.find(word, index)
            if index > -1:
                yield global_index + index
                index += 1

        global_index += len(line)




try:
    with open("filefilefile.txt", encoding = "utf-8") as file:
        a = find_word(file, "banana")
        print(list(a))
except FileNotFoundError:
    print('Файл не найден!')
except:
    print("Ошибка обработки файла!")
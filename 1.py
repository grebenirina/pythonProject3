'''
Создать программный файл F1 в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
Скопировать из файла F1 в файл F2 строки, начиная с четвертой по порядку.
Подсчитать количество символов в последнем слове F2
'''
with open("F1.txt", "w", encoding="utf-8") as f1:
    while True:
        line = input("Введите строку (пустая строка для окончания ввода): ")
        if line == "":
            break
        f1.write(line + "\n")
with open("F1.txt", "r", encoding="utf-8") as f1:
    with open("F2.txt", "w", encoding="utf-8") as f2:
        lines = f1.readlines()
        for i in range(3, len(lines)):
            f2.write(lines[i])
with open("F2.txt", "r", encoding="utf-8") as f2:
    words = f2.read().split()
    last_word = words[-1]
    num_characters = len(last_word)
print("Количество символов в последнем слове файла F2: ", num_characters)

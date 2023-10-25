'''
Сформировать (не программно) текстовый файл. В нём каждая строка должна
описывать учебный предмет и наличие лекционных, практических и лабораторных
занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для
каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество
занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)    10(лаб)
                                        Физкультура:      30(пр)
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
with open("subjects.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
subject_dict = {}
for line in lines:
    parts = line.split(":")
    name = parts[0].strip()
    lessons = parts[1].strip()
    lesson_parts = lessons.split()
    lecture = 0
    practice = 0
    lab = 0
    for part in lesson_parts:
        if "(л)" in part:
            lecture = int(part.split("(л)")[0])
        elif "(пр)" in part:
            practice = int(part.split("(пр)")[0])
        elif "(лаб)" in part:
            lab = int(part.split("(лаб)")[0])
    total_lessons = lecture + practice + lab
    subject_dict[name] = total_lessons
print(subject_dict)
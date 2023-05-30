import re
def z1():
    print(1)
    d = {'Россия': 'Москва', 'Беларусь':'Минск', 'Турция':'Анкара', 'Финляндия' :'Хельсинки', 'Китай':'Пекин', 'Ватикан':'Ватикан'}
    print(d)
    cap = input("Введите страну - ")
    for i in d:
        cap = re.sub(i, d[i], cap)
    print(cap)
    sort1 = sorted(d.keys())
    print(sort1)


import re
def z2():
    print(2)
    s = input()
    d = {'[АВЕИНОРСТавеинорст]': '1', '[ДКЛМПУдклмпу]': '2', '[БГЁЬЯбгёья]': '3', '[ЙЫйы]': '4', '[ЖЗХЦЧжзхц]': '5', '[ШЭЮшэю]': '8', '[ФЩЪфщъ]': '10'}
    for k in d:
        s = re.sub(k, d[k], s)
    print(sum(map(int, s)))

def z3():
    print(3)
    languages = set()
    chinese_speakers = []
    students = {'Артем': {'Англиский', 'Китайский', 'Русский'}, 'Вадим': {'Англиский', 'Французкий'}, 'Григорий': {'Китайский', 'Японский'}, 'Илья': {'Китайский', 'Русский'}, 'Сергей': {'Немецкий', 'Русский', 'Китайский'}}
    for student, lang in students.items():
        languages.update(lang)
        if 'Китайский' in lang:
            chinese_speakers.append(student)
        sorted_languages = sorted(list(languages))
        print(sorted_languages)
        print(chinese_speakers)

z1()
z2()
z3()
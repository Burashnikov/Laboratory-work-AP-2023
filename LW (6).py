import re
def z1():
    print('Выберите страну из списка')
    d = {'Россия' : 'Москва','Казахстан' : 'Нур-Султан', 'Беларусь' : 'Минск', 'Китай' : 'Пекин'}
    print(*d)
    capital = input("Введетие страну - ")
    for i in d:
        capital = re.sub(i, d[i], capital)
    print(capital)
    sort1 = sorted(d.keys())
    print(sort1)

import re
def z2():
    word = input("Введетие слово - ")
    d = {'[АВЕИНОРСТавеинорст]': '1', '[ДКЛМПУдклмпу]': '2', '[БГЁЬЯбгёья]': '3', '[ЙЫйы]': '4', '[ЖЗХЦЧжзхц]': '5', '[ШЭЮшэю]': '8', '[ФЩЪфщъ]': '10'}
    for k in d:
        word = re.sub(k, d[k], word)
    print(sum(map(int, word)))

def z3():
    languages = set()
    chinese_speakers = []
    students = {'Илья': {'Англиский', 'Китайский', 'Русский'}, 'Даша': {'Англиский', 'Французкий'},
                'Юля': {'Китайский', 'Японский'}}
    for student, lang in students.items():
        languages.update(lang)
        if 'Китайский' in lang:
            chinese_speakers.append(student)
        sorted_languages = sorted(list(languages))
        print(*sorted_languages)
        print(*chinese_speakers)

#z1(), z(2), z3()

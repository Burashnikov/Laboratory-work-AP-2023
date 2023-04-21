import re
def z1():
    d = {'Россия': 'Москва', 'Беларусь':'Минск', 'Турция':'Анкара', 'Финляндия' :'Хельсинки', 'Китай':'Пекин', 'Ватикан':'Ватикан'}
    print(d)
    cap = input("Введите страну - ")
    for i in d:
        cap = re.sub(i, d[i], cap)
    print(cap)
    sort1 = sorted(d.keys())
    print(sort1)

def z2():
    s = input("Введите слово - ")
    d = {'[АВЕИНОРСТавеинорст]': '1', '[ДКЛМПУдклмпу]': '2', '[БГЁЬЯбгёья]': '3', '[ЙЫйы]': '4', '[ЖЗХЦЧжзхц]': '5', '[ШЭЮшэю]': '8', '[ФЩЪфщъ]': '10'}
    for k in d:
        s = re.sub(k, d[k], s)
    print(sum(map(int, s)))

students = {

    "Бурашников": {"английский", "русский"},
    "Суворов": {"английский", "китайский", "японский"},
    "Андреев": {"английский", "немецкий", "французский"}

}

all_languages = set()
for languages in students.values():
    all_languages.update(languages)

print("Количество различных языков, которые знают студенты:", len(all_languages))
print("Отсортированный список языков, которые знают студенты:", sorted(all_languages))

chinese_speakers = []
for student, languages in students.items():
    if "китайский" in languages:
        chinese_speakers.append(student)

print("Список студентов, которые знают китайский язык:", chinese_speakers)

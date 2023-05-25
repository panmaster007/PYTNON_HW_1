# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

stih = list(input("Введите фразы Винни-Пуха: ").split(" "))
count = []
glasn_letter = ["а", "о", "У", "е", "ы", "э", "я", "и", "ю"]
def rhythm(tekst):
    m=0
    for x in stih:
        count.append(0)
        k=list(filter(lambda i: i in glasn_letter, x))
        count[m]=len(k)
        m+=1
    for i in range(len(count)-1):
        if count[i]!=count[i+1]:
            print("Пам парам")
            return
    print("Парам пам-пам")
    return
rhythm(stih)
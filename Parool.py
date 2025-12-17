import random

# Esimene näide: Parooli genereerimine
str0 = ".,:;!_*-+()/#¤%&"
str1 = '0123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()
str4 = str0 + str1 + str2 + str3
ls = list(str4)
random.shuffle(ls)
# Eemaldame nimekirjast 12 juhuslikku väärtust (Algselt: Извлекаем из списка 12 произвольных значений)
psword = ''.join([random.choice(ls) for x in range(12)])
# Parool on valmis (Algselt: Пароль готов)
print(psword)

import string
from random import choice

# Teine näide: Parooli genereerimine funktsioonina
def salasona(k: int):
    sala = ""
    for i in range(k):
        t = choice(string.ascii_letters) # Aa...Zz
        num = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        t_num = [t, str(num)]
        sala += choice(t_num)
    return sala

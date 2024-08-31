# 1. Добавить слово в конец списка так, чтобы каждая буква стала отдельным элементом списка
# l = [1, 2, 3]
# a = 'abc'
# result = [1, 2, 3, 'a', 'b', 'c']

l = [1, 2, 3]
a = 'abc'
result = l + list(a)
print(result)

# 2. Все чётные числа вывести в другой список
# l = [1,3,4,5,8,9,10,44,22,50,79,54,28,91]
# l = [x for x in l if x%2 == 0]

l = [1,3,4,5,8,9,10,44,22,50,79,54,28,91]
l2=[]
for m in l:
    if m%2==0: l2.append(m)
print(l2)

# 3. Все emails у которых есть слово test вывести в другой список
# l = ['webtest1@gmail.com',
#      'alex_dr5@gmail.com',
#      'elena_viktorovna@gmail.com',
#      'infotest@gmail.com',
#      'sigmatesst@gmail.com',
#      'planet.dollsatest@gmail.com',
#      'loadtestsinfo@gmail.com',
#      'straightwaytest@gmail.com',
#      'test.of.tests@gmail.com',
#      'bigmac@gmail.com',
#      'bigmactest@gmail.com',
#      'kfc_test_supply@gmail.com',
#      'cyberdesk@gmail.com',
#      'supportonlinetest@gmail.com'
#      ]

l = ['webtest1@gmail.com',
     'alex_dr5@gmail.com',
     'elena_viktorovna@gmail.com',
     'infotest@gmail.com',
     'sigmatesst@gmail.com',
     'planet.dollsatest@gmail.com',
     'loadtestsinfo@gmail.com',
     'straightwaytest@gmail.com',
     'test.of.tests@gmail.com',
     'bigmac@gmail.com',
     'bigmactest@gmail.com',
     'kfc_test_supply@gmail.com',
     'cyberdesk@gmail.com',
     'supportonlinetest@gmail.com'
     ]

l2=[]
text="test"
for x in l:
    if text in x:
         l2.append(x)
print(l2)

# 4. Найти самое маленькое число в списке
# l = [3,0,4,5,8,9,10,44,22,50,-1,79,54,-28,91]

l = [3,0,4,5,8,9,10,44,22,50,-1,79,54,-28,91]
print(min(l))

# 5. Сравнить 2 строки без учёта регистра
s1 = "Alex"
s2 = "alex"
if s1.upper() == s2.upper():
    print("Строки равны")
else: print("Строки не равны")

# 6. Проверить является ли массив подмножеством другого массива
# L1 = [1,4,6]
# L2 = [9,5,1,10,4,33,2,6,0,8]

L1 = [1,4,6]
L2 = [9,5,1,10,4,33,2,6,0,8]
x=0
for m in L1:
    if L2.count(m):
        x+=1
if x==len(L1):
    print("It`s ok.")
else:print("It`s wrong!")

# 7. Напишите функцию, которая принимает строку и
# возвращает количество букв английского алфавита,
# которые встречаются больше чем 1 раз.

print("Input a word:")
word = input().upper()
l = {}
word_set = set(word)
for x in word_set:
        if word.count(x) > 1:
            l[x] = word.count(x)
print(l)

# 8. Напишите функцию, которая принимает строки.
# Она должна вернуть False, если в строке содержится две одинаковые буквы в слове,
# а если таких слов нет — True.

# print(no_duplicate_letters('Здравствуйте, Александра'), '\n') 
# Две буквы "в" в "Здравствуйте," 
# False

# print(no_duplicate_letters('Всегда дожимай до конца'), '\n')
# True

print("Input text:")
text = input()
text_words = text.split()
undublicat = True
for word in text_words:
    for letter in word:
        if word.count(letter) > 1:
            print("False")
            undublicat = False
        break
if undublicat == True:
    print("True")


# 9. Напишите функцию, которая проверяет сложность пароля. Функция проверяет ряд условий и оценивает сложность пароля.
# За каждое выполненое условие пароль получает бал.
#
# Если выполняется одно условие - функция возвращает 1, если выполненяется 5 условий - функция вернет 5.
#
# Условия которые нужно проверить:
#
# длина пароля не меньше 6 символов,
# пароль содержит хотя бы 1 цифру,
# пароль содержит хотя бы одну заглавную букву,
# пароль содержит хотя бы одну строчную букву,
# пароль содержит хотя бы один из специальных символов: !@#$%^&*()-+
#
# Типы символов, которые будут содержаться в пароле во время тестирования:

# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"

# Пароль не должен содержать кириллических символов

ball0 = 0
ball1 = 0
ball2 = 0
ball3 = 0
ball4 = 0
word = []
rusNo_c = 0
print("Input a password:")
while word == [] or rusNo_c > 0:
    rusNo_c = 0
    pw = input()
    word = sorted(str(pw))
    if word == []:
        print("Password cannot be empty! Input a correct password:")
    if word != []:
        for n in list("йцукенгшщзхъфывапролджэячсмитьбю"):
            if word.count(n):
                rusNo_c += 1
                print("WRONG!!! Password contains \"cyrillic\"! Input a correct password:")
                break
if len(word) >= 6 and rusNo_c == 0:
    ball0 = 1
for n in list("0123456789"):
    if word.count(n):
        ball1=1
for n in list("abcdefghijklmnopqrstuvwxyz"):
    if word.count(n):
        ball2=1
for n in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    if word.count(n):
        ball3=1
for n in list("!@#$%^&*()-+"):
    if word.count(n):
        ball4=1

balls = ball0+ball1+ball2+ball3+ball4
if balls > 0 and rusNo_c == 0:
    print("Succses! Password balls: ", balls)

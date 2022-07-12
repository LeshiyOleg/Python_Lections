# print("hello World and Oleg")
# a = 123
# b = 1.23
# print(type(a))
# print(b)

# s = 'hello Oleg'
# print(s)  # вывод строки
# print(a, b, s)
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', '3', 'W', 1, 2, 4.5, True]

# list = ['1', '2', '3']
# print(list)
# col = ['hello', 1, 2, 4.5, True]
# print(col)

# print('Введите а');
# a = int(input())
# print('Введите b');
# b = int(input())
# # print(a, b)
# # print('{} -- {}'.format(a, b))
# print(a, '+', b, '=', a+b)

# a = 1.3123
# b = 3
# c = round(a * b, 5)
# print(c)

# a = 3
# a += 5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = 1 < 4 and 5>2
# print(a)
# b = 2
# c = 'qwe'
# print(b==c)
# d = [1,2]
# e = [2,1]
# print(d==e)

# func = 1
# T = 4
# x = 2
# print(func<T>(x))

# f = [1,2,3,4]
# print(f)
# print( not 2 in f)

# is_odd = f[1] % 2 == 0
# print(is_odd)

# is_odd = not f[1] % 2
# print(is_odd)

# Управляющие конструкции: if, if-else
# username = input('Введите имя: ')
# if(username == 'Маша'):
#  print('Ура, это же МАША!');
# else:
#  print('Привет, ', username);

# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

# Управляющие конструкции: while
# original = 235
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

# original = 237
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# else:
#  print('Пожалуй')
#  print('хватит )')
# print(inverted)

# Управляющие конструкции: for

# for i in 1, -2, 3, 14, 5:
#     print(i)

# list = [1,2,3,4,56,74,10]
# for j in list:
#     print(j)

# r = range(7)
# for l in r:
#     print(l)

# for i in range(1,10,2): # range(от, до, приращение)
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# # *****
# # *****
# # *****
# # *****
# # *****

# # Немного о строках
# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# Списки: введение

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# for e in colors:
#     print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент
# print(colors)

# Функции
# def f(x):
#     return x**2

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType
# def sum(x,y):
#     return x+y

# sum = lambda x, y: x+y +1

# def mult(x,y):
#     return x*y

# def calc(op, a, b):
#     print (op(a,b))
#     #return op(a,b)

# calc(lambda x, y: x+y +1, 4,5)

# list = []

# for i in range(1,101):
#     if(i%2 == 0):
#         list.append(i)
# print (list)

# def f(x):
#     return x**3

# new_list = [(i, f(i)) for i in range(1,21) if i%2 ==0]
# print (new_list)


# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# file = open('Lection_3\examp.txt', 'r')
# data = file.read()
# numbers_list = data.split()
# file.close()

# even_pow_list =[]
# for i in range(len(numbers_list)):
#     if numbers_list[i].isdigit():
#         numbers_list[i] = int(numbers_list[i])
#         if numbers_list[i] % 2 == 0:
#             even_pow_list.append((numbers_list[i], numbers_list[i]**2))
# print (numbers_list)
# print (even_pow_list)


# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(select(lambda x: (x, x**2), res))
# print (res)


# li = [x for x in range(1,20)]
# li = list(map (lambda x: x+10, li))
# print(li)


# data = map(int, input().split())

# for i in data:
#     print(i*10)
# data = list(map(int, input().split()))
# print(data)


# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print (res)


# # data = [x for x in range (10)]
# # res = list(filter (lambda x: not x%2, data))
# # print (res)

# # data = '1 2 3 5 8 15 23 38'.split()
# # res = map(int, data)
# # res = filter(lambda x: not x % 2, res)
# # res = list(map(lambda x: (x, x**2), res))
# # print (res)


# users = ['user1', 'user2','user3','user4','user5']
# ids = [4,5,9,14,7]
# salary = [111,222,333]
# data = list(zip(users, ids))
# print(data)
# data2 = list(zip(users, salary))
# print(data2)


users = ['user1', 'user2','user3','user4','user5']
data = list(enumerate(users))
print(data)
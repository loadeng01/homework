# num = 31
# def check(number):
#     if number %2 == 0:
#         print('Od')
#     elif number %2 == 1:
#         print('idi na ***  ')
#     else:
#         pass

# check(1)

# def is_palindrom(name):
#     if name == name[::-1]:
#         return True
#     else:
#         return False
    
# print(is_palindrom('myrk'))

# def world(num1,num2):
#     if num1 > num2:
#         return num1
#     elif num1 < num2:
#         return num2 

# print(world(1,5))



# num2 = [1,2,3,4,5]
# def num1(yu):  

#     num3 = 1
#     for i in yu:
#         num3 *= i
#     print(num3)
# num1(num2)
# print('ты стал немножко умнее')


# num = 34445

# def res(n:int):
#     ress = 0
#     for i in str(n):
#         ress += int(i)
#     return ress


# print(res(num))










# Создать функцию func11, которая будет принимать 3 числа в качестве аргументов,
# функция должна возвращать сумму первых двух чисел разделенную на третье число
# нужно реализовать проверку на то, что третье число не является нулем, если это ноль, то просто возвратить результат сложения первого и второго числа

# def name1(a,b,c):
#     if c == 0:
#         print(a+b)
#     else:
#         print((a+b)/c)
    
# print(0/0)









# Создать функцию func12, которая принимает в качестве аргумента список со строками и в каком регистре нужно вернуть данные, строки могут быть записаны в любом регистре, задача: на основе выбора регистра,
# возвращать либо список со строками в верхнем регистре, либо в нижнем регистре
# Например:

# func12(["hEllo", "wORld"], "lower") -> ["hello", "world"]


# def func12(words, werty):
#     q = []
#     if werty == "lower":
#         for i in words:
#             q.append(i.lower())
#         return q
#     elif werty == 'upper':
#         for i in words:
#             q.append(i.upper())
#         return q
    
# print(func12(["hEllo", "wORld"], "upper"))


# Создать функцию func13, которая будет принимать в качестве аргумента строку,
# а затем говорить сколько в ней и каких символов, результат вернуть в виде словаря
# Например:

# 'Hello' -> {'H': 1, 'e': 1, 'l': 2, 'o': 1}

# def fun13(str1: str):
#     return {x: str1.count(x) for x in str1}
# print(fun13('hello'))

# Создайте функцию-менеджер calc, которая будет принимать в себя два числа и операцию.
# Должны быть доступны операции(+, -, /, *).
# Создайте также 4 доп.функции - add_, sub_, div_, mult_, которые будут принимать в себя два числа.
# Затем в зависимости от операции calc будет вызывать одну из доп.функций.
# Соответственно, если операция '+', то вызывается функция add_ и т.д.


# dic = {'a': 1, 'b': 2, 'c':3}

# def fuck(kemal,nihan):
#     print(kemal+nihan)
#     print(kemal-nihan)

# fuck(1,3)
# fuck(1037, 74)

# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]

# def lis(dic):
#     hol = [a['name'] for a in dic if "IT" in a['work']]
#     return hol

# print(lis(users))




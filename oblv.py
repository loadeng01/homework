# пространсранство имен

# 1. builtins - встроенные функции и методы

# 2. global - это все перменные внутри файла которые мы создали

# 3. enclosed - пространство находящиеся между двумя пространствами(между global and local)

# 4.local - локальное пространство имен

# по мере выполнения программы python создает разные прострастранства имен и удаляет их

# globals - возвращает словать с глобальными переменными

# def hello():
#     a = "hola world"
#     print(locals())

# def func(a, b):
#     c = 5
#     print(locals())

# func(2, 7)

# enclosed - она возникает тогда когда есть вложенности в функции

# x = "global oblast"

# def func():
#     x = "it is enclosed"
#     print(x)
#     def func2():
#         x = "it is local oblast"
#         print(x)


# func()


# def func():
#     a = "func"
#     # enclosed
#     def inerfunc():
#         a = 'inerfunc'
#         # local
#         print(locals())
#     inerfunc()
#     print(locals())

# func()
# print(globals())


# a = 10
# def func():
#     b = 'local'
#     return a + 100

# print(a)
# print(func())


# local -> enclosed -> global -> builtins

# x = 10
# print(x, 'x is global')
# def func():
#     global x
#     x = 20
#     print(x, "x is enclosed")
#     def func2():
#         global x
#         x = 30
#         print(x, 'x is local')
#     func2()

# func()
# print(x, 'x is global')



# count = 0

# def counter():
#     print(count)
#     count += 1

# counter()

# count = 0

# def counter():
#     try:
#         print(count)
#         count += 1
#     except:
#         print('f')

# counter()

# count = 0

# def counter():
#     global count
#     count += 1
#     print(count)


# counter()
# counter()
# counter()


# def func():
#     a = 20
#     def inerfunc():
#         global a
#         a = 30
#         print(a, 'is local')
#     inerfunc()
#     print(a, 'is global')
    
# func()

# def func():
#     a = '1'
#     def inerfunc():
#         def inerfunc2():
#             nonlocal a
#             a = 2
#         inerfunc2()
#     inerfunc()
#     print(a)
# func()

# def enclosed():
#     x = 20
#     def local():
#         nonlocal x
#         x = 'Edited enclosed x'
#         print(x, 'is local')
#     local()
#     print(x, 'is enclosed')
# enclosed()

# def counter(a):
#     count = 0

#     def add():
#         nonlocal count
#         count += 1
#         print(count)

#     for x in range(a):
#         add()

# counter(10)



# def enclosed():
#     x = 20
#     def local():
#         nonlocal x
#         x = 30
#         print(x, 'is local')
#         def inerfunc():
#             nonlocal x
#             x = "Interstellar"
#             print(x)
#         inerfunc()
#     local()
#     print(x, 'is enclosed')

# enclosed()
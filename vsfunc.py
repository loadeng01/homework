# lambda = это анонимная функция (та же функция, но без названия)

# lambda параметр : что функция возваращает

# def add(a, b): 
#     return a + b

# res = lambda a, b : a + b


# print(res(3, 5))


# map(function, iterable obj) - функция которая принимает функцию и итерируемый объект
# она применяет функцию к каждому элементу передаваемового элемента

# maper = map(str, [1,2,3,4,5,6,7])
# print(tuple(maper))

# nums = [1,2,3,4,5,6]

# def func(num):
#     return num * num

# maper = list(map(func, nums))
# print(maper)



# lis = [1, -34, 12, -45, -19, 5]
# lambada = list(map(lambda x : x < 0, lis))
# print(lambada)

# func = lambda e : e + 1
# res = []
# for i in [1,2,3,4,5]:
#     res.append(func(i))

# print(res)


# filter(function, iterable) - функция принимает первым аргументом другую функцию и итерируемый объект
# результатом будет последовательность которая соответствовала условию filter

# nums = [*range(1, 11)]

# def folt(num):
#     if num % 2 == 0:
#         return True
    

# res = list(filter(lambda x : x%2 == 0, nums))
# print(res)

# def lno(word):
#     return len(word)

# lis = ["Алымбек", "Бека", "Константин", "Черт", "Володя"]

# sor = []
# for i in sorted(lis, key=len):
#     sor.append(i)

# print(sorted(lis, key=len))




# reduce - это фукция принимает фукнцию и возварщает один результат
# ее убрали из стандартной библиотеки Python так как ей нашли замену

# from functools import reduce

# lis = [*range(1, 7)]

# res = reduce(lambda x, y: x + y, lis)
# print(res)

# def ned(a, b):
#     return a * b

# res = reduce(ned, lis)
# print(res)


# enumerate(iterable, [с какого начинать элемента по дефолту 0])
# функция принимает последовательность и возвращает tuple состоящий из числа и элемента


# lis = ["deas", "freak", "interstellar", "dog", "hacker"]

# for i,s  in enumerate(lis):
#     print(i)

# for i in enumerate(lis[::-1]):
#     print(i)

# for i in enumerate(lis, 87):
#     print(i)

# lis = ["deas", "freak", "interstellar", ]

# res = list(enumerate(lis, 8))
# print(res)

# zip(iterable, iterables, ...) - сопостовялет каждый элемент из iterable со следующим

# lis1 = [*range(1, 5)]
# lis2 = ['a', 'b', 'c', 'd']
# print(dict(zip(lis1, lis2)))


# any(iterable) - возврощает True если хотя бы один элемент равен True
# all(iterable) - тоже самое что и any только наоборот


# tery = all([True, True, True])
# print(tery)

# lis = [1, -34, 12, -45, -19, 5]
# lambada = list(map(lambda x : x < 0, lis))
# print(lambada)

# dict_ = {1: 2, 3: 4, 5: 6}
# dict_ = list(map(lambda x: str(x) , dict_.values()))
# print(dict_)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = list(map(lambda x : 'четное' if x % 2 == 0 else 'нечетное', lst))
# print(res)


# dic = {1:22, 2:4, 3: 23}
# dic.setdefault(5, 999)
# print(dic)



# lis = [10, 23, "world", -2, 33, "hello", "demo"]

# res = list(filter(lambda x: type(x) == int, lis))
# res2 = list(map(lambda x: x**0.5, res))
# # res3 = list(map(lambda x: round(x, 3), res2))

# print(res2)

# from functools import reduce

# words = ['a', 'b', 'c', 'd', 'e']

# res = reduce(lambda x, y: x + y, words)
# print(res)

# a = {'a': 1}

# print(a['a'])

# a = [1,2,3,34,4]
# a.append( "asd")
# print(a)


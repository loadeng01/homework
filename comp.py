# comprehension = генерация последовательности в одну строку используя цикл
# основной целью использования как list, dict comprehension является упрощение и повышение читаемости кода

# list comprehension - это упрощенный подход к созданию списка, который задействует цикл for, а так же if else операторы


# for i in range(1, 11):
#     lit.append(i)

# print(lit)


# import time

# star = time.time()
# lit = [i for i in range(100)]


# time1 = time.time() - star
# print(time1)


# lit = [i for i in range(1, 11) if i%2 == 0]
# print(lit)


# print(input() for i in range(10))

# если в условии нужен else, то все условие пишется до for

# lit = ["nechet" if i % 2 else "chet" for i in range(1, 11)]
# print(lit)

# lit = [1, "hola", 2, "sada", 312, "maza", 2.332]

# num = ["nechet" if i % 2 else "chet" for i in lit if type(i) == int or type(i) == float]
# print(num)


# set comprehension
# разница с list compr что выходные данные не содержат дубликаты

# dict comperhension - создаются так же, но обязательно нужно указывать ключи и значения

# frd = dict()

# lit = [1,2,3,4,5,6,7]

# dictt = {i: lit.count(i) for i in lit}
# print(dictt)
# dic = {"dae": 23, "asd": 45, "frog": 412}

# di = {k: "nechet" if v % 2 != 0 else "chet" for k, v in dic.items()}
# print(di) 

# dic = {i: str(i) for i in range(6)}
# print(dic)

# dic = {list1[i]: list[2] for i in range(len(list1))}


# dic = {"dae": 23, "asd": 45, "frog": 412}
# dic2 = {k: v for k, v in dic.items()}
# print(dic2)


# dic = {"dae": 23, "asd": 45, "frog": 412}
# dic2 = {v: k for k, v in dic.items()}
# print(dic2)

# dict1 = {
#     "a":[1,2,3,4,5],
#     "b":[10,30,2,5],
#     "c":[74,28,47],
#     "d":[4,6,2,92,9]
#     }

# dic2 = {k: sum(v) for k, v in dict1.items()}
# print(dic2)


# lit2 = [["helloworld" for i in range(5)] for i in range(10)]
# print(lit2)




# word = "#makers#bootcamp#программирование#it#курсы".split("#")
# word.pop(0)
# print(word)



# word = input("Word: ")

# if len(word) >= 5:
#     print(True)
# else:
#     print(False)


# num = int(input("Number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative") 
# elif num == 0:
#     print("Zero")


# num = int(input("Number 1-12: "))

# if num == 12 or num == 1 or num == 2:
#     print("Зима")
# elif num == 3 or num == 4 or num == 5:
#     print("Весна")
# elif num == 6 or num == 7 or num == 8:
#     print("Лето")
# elif num == 9 or num == 10 or num == 11:
#     print("Осень")
# else:
#     print("Такого месяца нет")


# words = ['yes', 'no', 'maybe', 'ok', 'what']
# nums = [len(i) for i in words]

# print(words)
# print(nums)


# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = [i for i in nums if i < 5]

# print(res)


# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {key: val if val % 2 else 2 for key, val in a.items()}

# print(a)
# print(b)


# list_ = [i if i%2 else True for i in range(1, 11)]
# list_ = [i if type(i) != int else False for i in list_]

# print(list_)


# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = ["shorter" if len(i) <= 4 else "longer" for i in list_name]
# print(new_list)

# dict_ = {k: k ** 2 for k in range(1, 11)}
# print(dict_)

# n = int(input("N: "))
# dict_ = {i: i ** 2 for i in range(n, 500, n)}
# print(dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: [v for v in range(1, v + 1)] for k, v in a.items()}
# print(dict_)


# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k: "odd" if v % 2 else "even" for k, v in dict_.items()}
# print(a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# lis = string_.split(" ")

# list_ = [i for i in lis if i.isdigit()]
# print(list_)


dict_ = {
'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
'Nik': {'history': 84, 'math': 85, 'literature': 87}
}

dic = {k: v for k, v in dict_.items() for k,v in dict_.items()}
print(dic)


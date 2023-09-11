# def my_len(obj):
#     count = 0
#     for element in obj:
#         count += 1
#     print(count)


# strong = 'string'
# my_len(strong)

# функции - это именнованый блок кода, ктоторый выполняет одну задачу и может принимать в себя аргументы
# и возвращает какое то значение
# функцию можно вызывать много раз


# def - ключевое слово которое указывает питону что я хочу создать функцию
# дальше идет название переменной
# скобки - нужны для того чтобы функция могла принимать параметры

# синтаксис

# def name_func(args):
#     принимает аргументы для работы в теле name_func
#     тело функции

# def my_sum(x, y):
#     print(x + y)
#     return "hui"

# res = my_sum(5, 4)
# print(res)

# распаковка

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {**dict1}
# print(dict2)

# необязательные аргументы args kwargs
# args = принимает позиционные аргументы
# kwargs = принимает именнованные аргументы

# arga = tuple
# kwargs = dict

# def two_sum(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)
#     return a + b + sum(args) + sum(kwargs.values())

# print(two_sum(2,3,4,6,4,3,2,4,5,6,7,6,4,3,3, first=100, second=200, third=300))


# def func(a, b=10, *args, **kwargs):
#     print("a", a)
#     print('b', b)
#     print('args == ', args)
#     print('kwargs == ', kwargs)

# func(3,5,6,7)


# аннотации - они делают код более информативным

# num: int = 10
# str_: str = "hola"


# lis = ['kek', 'nolon', 'hola', 'getteg']

# def palindrom(words: list) -> list:
#     palindrom1 = []

#     for word in words:
#         if word == word[::-1]:
#             palindrom1.append(word)
#         else:
#             continue
    
#     return palindrom1

# print(palindrom(lis))


# dic = {'a': 1, 'b': None, 'c': 3, 'e': None}

# def rem_none(a: dict) -> dict:
#     rem = {}
#     for k, v in a.items():
#         if v != None:
#             rem[k] = v
#         else:
#             continue
#     return rem

# print(rem_none(dic))

# def valide(email: str) -> bool:
#     index = email.find("@")
#     domains = 'gmail.com'
#     if "@" not in email:
#         raise Exception('Invalid email, whithout "@"')
#     elif not email[:index]:
#         raise Exception('Invalid email')
#     elif email[index+1:] not in domains:
#         raise Exception(f'Invalid email domain {domains}')
    
#     print("Email is good and saved")
#     return True



# def register(email:str, password1: str, password2: str) -> dict:
#     db_email = None
#     password = None
#     if valide(email):
#         db_email = email
#     if password1 != password2:
#         raise Exception("пароли не совпадают")
#     password = password1
#     msg = "Вы успешно зарегались"
#     return {'email': email, 'password': password, "msg": msg}

# email = input("Email: ")
# password1 = input("Password: ")
# password2 = input("Repeat password:")
# print(register(email, password1, password2))



# def plus(a: int, b: int):
#         result = a + b
#         print(result)

# try:
#     num1 = int(input("Num 1: "))
#     num2 = int(input("Num 2: "))

# except ValueError:
#     print("Вводите только числа")
# else:
#     plus(num1, num2)



# def my_len(word: str):
#     """
#     Данный метод считает длину строки не считая пробелов
#     """
#     count = 0
#     for element in word.replace(' ', ''):
#         count += 1
#     print(count)


# word = input("Введите слово или предлодение: ")
# my_len(word)


# num = {'a': 123}
# word = 'ded'

# def typer(a, b):
#     print(f"У первой переменной тип данных {type(a)}")
#     print(f"У второй переменной тип данных {type(b)}")


# typer(num, word)


# def division(a: int, b: int):
#         result = a / b
#         print(round(result, 2))

# try:
#     num1 = int(input("Num 1: "))
#     num2 = int(input("Num 2: "))
#     result = a / b

# except ValueError:
#     print("Вводите только числа")
# else:
#     print(round(result, 2))


# num = 12
# dit = {'a': 1, 'b': 2, 'c': 4, 'd': 8}

# def keypr(dict_: dict):
#     for k in dict_:
#         print(k)

# keypr(dit)

# def evens(num: int):
#     if num % 2 != 0:
#         print("It's odd number")
#     else:
#         print("It's even number")


# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Вводите только числа")
# else:
#     evens(number)


# def palindrom(word: str) -> bool:

#     if word.replace(' ', '') == word[::-1].replace(' ', ''):
#         return True
#     else:
#         return False
    
# word = input("Word: ")
# print(palindrom(word))




# def get_max(a: int, b: int) -> int:
#     if a > b:
#         return a
#     elif b > a:
#         return b
#     else:
#         return a


# try:
#     num1 = int(input("Num 1: "))
#     num2 = int(input("Num 2: "))

# except ValueError:
#     print("Вводите только числа")
# else:
#     print(get_max(num1, num2))



# def multiplic(nums: list) -> int:
#     summ = 1
#     for i in nums:
#         summ *= i

#     return summ

# nums = [1,2,3,4,5]
# print(multiplic(nums))





# def get_sum(nums: int) -> int:
#     summ = 0
#     str_nums = str(nums)
#     list_int = []
#     list_int.extend(str_nums)

#     for i in list_int:
#         summ += int(i)

#     return summ

# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Вводите только числа")
# else:
#     print(get_sum(number))


# nums = [1, 3, 2, 5, 4, 3, 6, 7, 4, 3, 2, 1, 2, 2, 2, 2]

# def resort(nums: list) -> list:
#     for i in nums:
#         if nums.count(i) > 1:
#             while nums.count(i) != 1:
#                 nums.remove(i)

#     nums.sort(reverse=True)
    
#     return nums

# print(resort(nums))

# def sum_range(start: int, end: int) -> int:
#     if start > end:
#         start, end = end, start
#         return sum([i for i in range(end, start + 1)])
    

# print(sum_range(2, 4))



# def get_sum(num: int) -> int:
#     dict_ = []

#     for i in range(1, 1000):
#         if num % i == 0:
#             dict_.append(i)

#     return dict_

# print(get_sum(1098))

# import random

# def generate_password(name: str) -> str:
#     num = str(random.randint(1000000, 10000000))
#     return name + num

# def get_info(name: str, surname: str) -> str:
#     full_name = name + surname
#     return generate_password(full_name)

# try:
#     name = input("Ваше имя: ").title().replace(" ", "")
#     surname = input("Ваша фамилия: ").title().replace(" ", "")

#     if name == "" or surname == "":
#         raise ValueError
# except ValueError:
#     print("Нельзя оставлять строку пустой!")
# else:
#     print(get_info(name, surname))


# def get_data(num1: int, num2: int, action: str) -> int:
#     if "+" in action:
#         return num1 + num2
#     elif "-" in action:
#         return num1 - num2
#     elif "*" in action:
#         return num1 * num2
#     elif "/" in action:
#         return round(num1 / num2, 3)
#     return 0

# def result(num: int) -> int:
#     print()

# while True:   
#     try:
#         num1 = int(input("Первое число: "))
#         num2 = int(input("Второе число: "))
#         act = input("Действие: ")
        
#         if act not in "+ - * /":
#             raise TypeError
#     except TypeError:
#         print("К сожалению у нас нет других действий")
#     except ValueError:
#         print("Пишите только числа")
#     else:
#         print("Ответ:", get_data(num1, num2, act))
#     finally:
#         print("<========================>")
    
#     check = input("Хотите продолжить? Y/N: ").title()
#     if check in "N":
#         break
#     else:
#         continue



# def plus(num1: int, num2: int) -> int:
#     return num1 + num2

# def minus(num1: int, num2: int) -> int:
#     return num1 - num2

# def mult(num1: int, num2: int) -> int:
#     return num1 * num2

# def division(num1: int, num2: int) -> int:
#     return round(num1 / num2, 3)

# def get_data(num1: int, num2: int, action: str) -> int:
#     if "+" in action:
#         return plus(num1, num2)
#     elif "-" in action:
#         return minus(num1, num2)
#     elif "*" in action:
#         return mult(num1, num2)
#     elif "/" in action:
#         return division(num1, num2)
#     return 0

# def result():
#     print("Ответ:", get_data(num1, num2, act))

# while True:   
#     try:
#         num1 = int(input("Первое число: "))
#         num2 = int(input("Второе число: "))
#         act = input("Действие: ")
        
#         if act not in "+ - * /":
#             raise TypeError
#     except TypeError:
#         print("К сожалению у нас нет других действий")
#     except ValueError:
#         print("Пишите только числа")
#     else:
#         result()
#     finally:
#         print("<========================>")
    
#     check = input("Хотите продолжить? Y/N: ").title()
#     if check in "N":
#         break
#     else:
#         continue
    


dict_ = {"a": 1, "b": 2, "c": 3}

def dictionary(words: dict):
    for k in words:
        print(k)

dictionary(dict_)

    


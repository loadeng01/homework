# def decor(func):
#     print("decor func")
#     return func()


# def func():
#     print("func")
#     return "hello"

# res = decor(func)
# print(res)


# decorator = это функция которая принимает другую функцию

# Декоратор ялвляется высшего порядка (значит может принять функцию как аргумент и вернуть ее)

# декоратор модифирует и улучшает принятую функцию и выдает измененную

# def deco(func):
#     print("я буду работать до функции func1")
#     print(func())

# def func1():
#     return "функция deco завершилась"

# deco(func1)

    
# def upper(func):
#     def wrapper():
#         original_res = func()
#         modified_res = original_res.upper()
#         return modified_res
#     return wrapper()

# @upper
# def text():
#     return "Devil may cry"

# @upper
# def text2():
#     return "Angel don't may cry"



# print(text)
# print(text2)



# def decor(func):
#     def wrapper(info):
#         return "Вы передали " + str(func(info))
#     return wrapper

# @decor
# def get_name(name):
#     return name
# @decor
# def get_age(age):
#     return age
# @decor
# def get_last_name(last_name):
#     return last_name

# print(get_age(22))
# print(get_name("Не хочу"))
# print(get_last_name("Не скажу"))




# def func(f): # сюда попадает функция которую нужно задекорировать
#     def wrapper(): # оберточная оболочка для функции
#         print('Я код, который отрабатывает до вызова функции')
#         f()
#         print("а я код который сработает после вызова функции")
#     return wrapper  # мы возвращаем обертку


# @func
# def fun(): # функция которую мы задекорируем
#     print("Шалом евреи")

# fun()


# если мы используем аргументы у функции, то мы обязательно должны передавать их в декоратор

# def decor(func):
#     def wrapper(arg):
#         print(f"Смотри что я принимаю {arg}")
#         func(arg)
#     return wrapper


# @decor
# def fun(word: str):
#     print(f'Я принимаю в себя слово {word}')

# fun("Intersterllar")


# def decorator(func): # лучше использовать такую запись потому что она является универсальной для всех функций
#     def wrapper(*args, **kwargs):
#         print(f'здесь args {args}')
#         print(f'здесь kwargs {kwargs}')
#         func(*args, **kwargs)
#     return wrapper

# @decorator
# def func1():
#     print("Функция без параметров")

# @decorator
# def func2(name: str, last_name: str):
#     print("Функция с параметрами")
#     print(f'Дарова {name} {last_name}')

# @decorator
# def func3(name: str, last_name: str):
#     print("Функция с параметрами")
#     print(f'Дарова {name} {last_name}')


# func1()
# func2("Black", "Jack")
# func3(name="Jack",last_name="Black")


# def div(func):
#     print("f1")
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return '<div>' + func(*args, **kwargs) + '</div>'

#     return wrapper

# @div
# def get(name, name2):
#     print("f2")
#     return name + name2

# print(get('John', 'Snow'))


# def decor(func):
#     print("я декоратор, я буду вызван в момент декорации функции")
#     def wrapper():
#         print("Я функция обертка, вызываюсь каждый раз при декорировании функции")
#         return func()
#     print("я возвращаю обернутую функцию")
#     return wrapper

# @decor
# def func():
#     print("Я декорированная функция")


# func()



# def benchmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"функция отработала: {end - start}")
#     return wrapper

# @benchmark
# def webpage():
#     import requests
#     webpage = requests.get("https://google.com")


# @benchmark
# def iterate():
#     for i in range(50001):
#         print('иди на хуй')


# print()




# исключения и ошибки - это объекты которые прерывают работу кода

# ошибки - это больше ошибки в синтаксисе (которые мы исправляем самостоятельно)

# Эти ошибка обработать нельзя

# 1. SyntaxError - синтаксическая ошибка: забыли что двоеточие, неправильно назвали переменную и тд.

# 2. IndentationError - ошибка табуляции и неправильный отступ

# 3. TabError - это неверная табуляция, смешивание tab и пробела 


# исключения - это когда код написан верно, но программа работает не так как ожидалось

ZeroDivisionError # - выходит при делении на 0
NameError # - исключение выходит когда обращаемся к несуществующей переменной
IndexError # - исключение которое выходит когда обращаемся к несуществующему индексу
KeyError # - исключение которое выходит когда мы обращаемся к несуществующему ключу
ImportError # - исключение которое выходит когда мы импортируем несуществующий модуль или функцию
ValueError # - когда в фунцию передаем не тот тип данных
TypeError # - когда мы пытаемся использовать методы не свойственные какому то типу данных 
# либо же когда мы передаем в функцию больше или меньше аргументов чем ожидает
AttributeError # - выходит когда мы обращаемся к несуществующему аттрибуту или объекту
BaseException # - отец ошибок


# try except 
# мы используем это строение чтобы наш код не прекращал нашу работу

# try:
#     # код который может вызвать ошибку
# except:
#     # код который сработает если в try вышла ошибка
# else:
#     # код который сработает если в try не вышла ошибка
# finally:
#     # код который сработает в любом случае



# while True:
#     try:
#         age = int(input("Введите возраст: "))
#     except ValueError:
#         print("Писать научись")
#     else:
#         print(f"Хорош, тебе {age}")
#         break
#     finally:
#         print("<================================>")

# try:
#     a = int(input("a: "))
#     b = int(input("b: "))
#     result = a // b
# except ZeroDivisionError:
#     print("Дебил на ноль делить нельзя!")
# else:
#     print(result)

# try:
#     while True:
#         print("F")
# except KeyboardInterrupt:
#     print("Красава что остановил это дерьмо")


# try:
#     int("24ws")
# except ValueError as e:
#     print(e)
#     print("так нельзя")
#     try:
#         3 / 0
#     except ZeroDivisionError:
#         print("dds")

# while True:
#     try:
#         num1 = int(input("n1: "))
#         num2 = int(input("n2: "))
#         result = num1 / num2
#     except ZeroDivisionError:
#         print("Дебил на ноль делить нельзя!")
#     except ValueError:
#         print("Буквы писать нельзя, гуманитарий хуев")
#     else:
#         print(round(result, 2))


# try:
#     num1 = int(input("n1: "))
#     num2 = int(input("n2: "))
#     result = num1 / num2
#     print(result)
# except ValueError:
#     print("ты ввввввел неправильно данные")
# except ZeroDivisionError:
#     print("Дебил на ноль делить нельзя!")




# raise - искуственно вызывает ошибку

# try:
#     val1 = input("n1: ").replace(" ", "")
#     val2 = input("n2: ").replace(" ", "")
#     result = 0

#     if val1 == "" or val2 == "":
#         raise Exception
    
#     result = int(val1) + int(val2)

# except ValueError:
#     print(f"Результат: {val1 + val2}")

# except Exception:
#     print("Строка пустая! Напишите что нибудь")

# else:
#     print(f"Результат: {result}")




# users = {12954: "John", 31369: "Damian", 40575: "Christopher", 43617: "Daniel"}
# names = [v for v in users.values()]
# ids = [k for k in users]
# print(names)

# try:
#     name = input("Ваш юзернейм: ").title()
#     user_id = names.index(name)
# except ValueError:
#     print("Введенного юзера нет в базе данных")
# else:
#     print(f"Приветствуем вас {name}, ваш ID {ids[user_id]}")
# finally:
#     print("Спасибо!")




# try:
#     age = int(input("Ваш возраст: "))
#     if age <= 0:
#         raise Exception
# except ValueError:
#     print("Вводите только числа!")
# except Exception:
#     print("Ваш возраст должен быть больше 0")
# else:
#     print(f"Ваш возраст {age}")





# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 'Nik': {'history': 84, 'math': 85, 'literature': 87}} 


# new_dict={x:max(y,key=lambda x:y.get(x)) for x,y in dict_.items()} 
# print(new_dict)

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}

# dict_ = {k: (v for v in v.values()) for k, v in my_dict.items()}
# print(dict_)


# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k:y for k,v in my_dict.items() for x,y in v.items()} 
# print(dict_)

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# num = [y for k,v in dict_.items() for x,y in v.items()]
# print(num)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# dict_ = {i: len(i)**2 for i in list_name if len(i) > 4}
# print(dict_)

# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }

# num = [y for k,v in dict_.items() for x,y in v.items()]

# new_dict = [v['likes'] for k,v in dict_.items() if v['rating'] > 3]
# print(sum(new_dict))


# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }

# dict1 = [b['id'] for value in dict_.values() for b in value['comments'] if len(value['comments']) > 3] 
# print(dict1)

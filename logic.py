
# list_ = list(input("nums:").replace(",", ""))
# tuple_ = tuple(list_)

# print(list_)
# print(tuple_)

# num = int(input("Num: "))

# if num%2 == 0:
#     print("Число четное")
# else:
#     print("Число нечетное")

# import random

# num = random.randint(1, 5)
# unum = int(input("Num: "))
# print(num)

# if unum == num:
#     print("Угадал")
# else:
#     print("Не угадал")


# ТЕРИНАРНЫЕ ОПЕРАТОРЫ

# a = 3
# res = "Hola" if a == 3 else "Bye"
# print(res)


# МАРЖОВЫЕ ОПЕРАТОРЫ

# маржовые оператор позвляет нам как присваивать значение переменной так и возвращать ее

# print(num := 3)



# operator = input("Введите оператор: ")
# num1 = int(input("Num 1: "))
# num2 = int(input("Num 2: "))

# if "+" in operator:
#     print(num1 + num2)
# elif "-" in operator:
#     print(num1 - num2)
# elif "/" in operator:
#     print(num1 / num2)
# elif "*" in operator:
#     print(num1 * num2)
# else:
#     print("Ашибка")


# num = int(input("Num: "))

# if (num % 3 == 0) and (num % 5 == 0):
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)



# list_ = [1, 2, 3, 4, 5]
# new_list = []

# for i in list_:
#     new_list = str(i)




# name = input("Имя: ")
# num = int(input("Число: "))

# friend = "друг" if num < 2 else "друзей"
# print(f"У {name} {num} {friend}")


# numx = int(input("x" ))
# numy = int(input("y" ))
# numz = int(input("z" ))


# if numx == numy and numx == numz:
#     print("треугольник равносторонний")
# elif numx == numy or numx == numz or numy == numx:
#     print("треугольник равнобедренный")
# else:
#     print("треугольник разносторонний")


# password = input("Your password: ")


# if len(password) < 8:
#     print("У вас недотаточно символов")
# elif password.isupper == False:
#     print("В вашем пароле нет заглавных букв")
# elif password.islower == False:
#     print("В вашем пароле нет сторочных букв")





# word = "Intersterllar"
# print(word[-1])
# print(word[-2:])
# print(word[::-1])
# print(len(word))

# word = "The quick brown fox jumps over the lazy dog".replace("o", "*")
# print(word)

# name = input("Имя: ")
# surname = input("Фамилия: ")
# age = int(input("Возраст: "))
# city = input("Город проживания: ")

# result = f"Вас зовут {name} {surname}, Ваш возраст: {age}, Вы проживаете в городе {city}"
# print(result)


# word = input("Ваше слово: ")

# if len(word) >= 5:
#     print(True)
# elif len(word) < 5:
#     print(False)



# num = int(input("Num: "))

# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")


# age = int(input("Возраст: "))
# dog_age = int

# if age <= 2:
#     dog_age = age * 10.5
#     print(dog_age)
# elif age > 2:
#     dog_age = (age * 4) + 13
#     print(dog_age)


# password = input("Password: ")

# if len(password) < 8 and password.isdigit() == False:
#     print("Ваш пароль должен содержать минимум 8 символов")
#     print("Ваш пароль должен содержать только числа")
# elif len(password) < 8:
#     print("Ваш пароль должен содержать минимум 8 символов")
# elif password.isdigit() == False:
#     print("Ваш пароль должен содержать только числа")
# else:
#     print("Ваш пароль сохранен")


# nums = input("Введите свои баллы по математике, английскому языку и литературе через запятую: ").split(",")

# num1 = int(nums[0])
# num2 = int(nums[1])
# num3 = int(nums[2])

# average = (num1 + num2 + num3) // 3

# if average > 69:
#     print("Вы допущены к экзаменам. Ваш средний балл составляет: ", average)
# else:
#     print("У вас недопуск к экзаменам! Ваш средний балл составляет: ", average)




# import random

# game = ["Камень", "Ножницы", "Бумага"]

# user = input("Ваш выбор: ").title()
# comp = random.choices(game)
# print("Выбор компа: ", comp)

    
# if game[0] in user:
#     if game[0] in comp:
#         print("Ничья!")
#     elif game[1] in comp:
#         print("Вы выиграли!")
#     elif game[2] in comp:
#         print("Вы проиграли!")
# elif game[1] in user:
#     if game[0] in comp:
#         print("Вы проиграли!")
#     elif game[1] in comp:
#         print("Ничья!")
#     elif game[2] in comp:
#         print("Вы выиграли!")
# elif game[2] in user:
#     if game[0] in comp:
#         print("Вы выиграли!")
#     elif game[1] in comp:
#         print("Вы проиграли!")
#     elif game[2] in comp:
#         print("Ничья!")
# else:
#     print("Такого предмета нет!")


# das = "ukulele"
# da = []
# for i in range(len(das)):
#     da += das[i] + "&"

# print(da)


# list_ = [23, 34, 54, 1, 2, 3, 4, 5]
# new_list = []


# for i in list_:
#     if i % 2 == 0:
#         new_list += ['четное']
#     elif i % 2 != 0:
#         new_list += ['нечетное']


# print(new_list)


# list1 = [23,24543,46,56,7]
# list2 = [23,24543,46,56,5]

# sum1 = sum(list1)
# sum2 = sum(list2)
# print(sum1 + sum2)


# list_ = input().split(",")

# list_.sort()
# print(list_)













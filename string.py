"""
строки - неизменяемый тип данных, предназначены для хранения текста
и они заключаются в одинарные или двойные кавычки

string = 'строка с одинарными'
string = "строка с двойными"
string = "'Don't do that'"

нельзя конкатенировать с другими типами данных
"""

# st = """
# sr[fdsfsd]
# sdfsd
# sdffsdgfgd
# """

# print(st)


    #    ФОРМАТИРОВАНИЕ СТРОК


"""
1.форматирование с использованием %
2. с использованием метода .format
3.Интерполяция строк (f-строки)
"""

# name = input("Write something: ")
# result = "<-| wow, you write: %s |->" % name
# print(result.upper())

# ward = input("So, what is your name?: ")
# result = "welcum to the club,  {}".format(ward) 
# print(result)

# ward = input("Name?: ")
# result = f"Hola {ward}"
# print(result)

"""
методы типов данных = фукнции, к которые мы обращаемся через точку
"""
# методы на is
# check = "esfrredsf"
# print(check.isdigit()) - проверяет на то состоит ли полностью из цифр

# check = "esfrredsf"
# print(check.isalpha()) - проверяет на буквы

# check = "@"
# print(check.isalnum()) - проверяет на наличие букв и цифр

# batcat = """
#      
#                          /\       /\ 
#                        _/  \ ___ /  \_ 
#                      /                 \ 
#                     /   /\        /\    \ 
#                    /                     \ 

# """
# print(batcat)


# print("sfrrsdfedsf".replace('s', 'GG'))


# a = "Interstellar good movie"
# print(a.join(" "))
# print(test[-1] + test[1:4] + test[0])

# adress = "1.1.1.1"
# print(adress.replace(".", "[.]"))

# string1 = "America"
# string2 = "Japan"
# num1 = round((len(string1) - 1) / 2)
# num2 = round((len(string2) - 1) / 2)
# print(string1[0] + string2[0] + string1[num1] + string2[num2] + string1[-1] + string2[-1])


# string = "          Как прекрасен этот мир!   "
# str = string.lstrip().rstrip()
# print(f"{str}\n{len(str)}")


# num = int(input("Num: "))

# check = chr(num)

# if check.isalpha() == True:
#     print(f'Это буква "{check}"')
# elif check.isalpha() == False:
#     print(f'Это символ "{check}"')


# greeting = input("h: ")

# if "Hi" in greeting:
#     print("Hello")
# else:
#     print("NO")


# count = 0
# number = input("G:")

# if number.isalnum() == True:
#     count = int(number)
#     print(count)
# elif count < 0:
#     print(0)
# else:
#     print(count)

# string = "123456"

# str1 = int(string[0])
# str2 = int(string[1])
# str3 = int(string[2])
# str4 = int(string[3])
# str5 = int(string[4])
# str6 = int(string[5])

# num1 = str1 + str2 + str3
# num2 = str4 + str5 + str6

# if num1 == num2:
#     print("да")
# else:
#     print("нет")

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# d = [a, b, c]
# df = sorted(d)
# print(df[0], df[1], df[2])



# num = int(input("num: "))

# if num == 1 or num == 2 or num == 12:
#     print("зима")
# elif num == 3 or num == 4 or num == 5:
#     print("весна")
# elif num == 6 or num == 7 or num == 8:
#     print("лето")
# elif num == 9 or num == 10 or num == 11:
#     print("осень")
# else:
#     print("Такого месяца нет")



# a = int(input("")) 
# b = int(input("")) 
# c = int(input("")) 

# if (a + b) > c and (a + c) > b and (b + c) > a: 
#     print("yes") 
# else: 
#     print("no")


# a = int(input("a: ")) 
# b = int(input("b: "))
# c = int(input("c: "))

# rect = (a ** 2) == (b ** 2) + (c ** 2)
# obt = (a ** 2) > (b ** 2) + (c ** 2)
# act = (a ** 2) < (b ** 2) + (c ** 2)

# if rect == True:
#     print("rectangular")
# elif obt == True:
#     print("obtuse")
# elif act == True:
#     print("acute")
# else:
#     print("impossible")



# a1, b1, c1 = int(input()), int(input()), int(input()) 
# c = max(a1, b1, c1) 
# b = min(a1, b1, c1) 
# a = sum([a1, b1, c1]) - min(a1, b1, c1) - max(a1, b1, c1) 

# if c >= a + b: 
#     print('impossible') 
# elif c**2 == a**2 + b**2: 
#     print('rectangular') 
# elif c**2 < a**2 + b**2: 
#     print('acute') 
# elif c**2 > a**2 + b**2: 
#     print('obtuse')

# book = "ksdjnflsdimfdf. sodinfoidsnfoisndf. sodifodsijfpoisjdf."
# print(book.count("."))


# book = "  Magnum , Fast , Domminik  "
# book2 = book.replace(" ", "")
# book3 = book2.split(",")
# print(len(book3))
# print(book3)


# alname = input("name: ").split()
# print(f"{alname[0]} {alname[1][0]}. {alname[2][0]}.".title())



# book = input("Word: ")

# if "сок" in book:
#     print(True)
# else:
#     print(False)


# num = int(input("N: "))

# if (num % 2) == 0:
#     print("второй")
# else:
#     print("первый")


# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if x1 == x2 or y1 == y2:
#     print("YES")
# else:
#     print("NO") 


# name = input("Имя, Фамилия и возраст через пробел: ").split()
# name1 = name[0].replace("a", "").capitalize()
# age = int(name[2])
# print(name1*age)
# numname = int(len(name[1]))
# num = "*".join(name[1][i*1:(i+1)*4] for i in range(1))
# print(num)

# number = '1234123412341234'
# number_ = ' '.join(number[i*4:(i+1)*4] for i in range(4))
# print(number_)





# word = input("Word: ")
# book1 = set("eyuioa")
# book2 = set("аияуюоеэ")

# num = 0

# for i in word:
#     if i in book1:
#         num += 1
#     elif i in book2:
#         num += 1
    
# print(f"В вашем слове {num} гласных")


# name = input("Username: ")
# mid = int(len(name) / 2) 
# password = name[:mid] + "&" + name[mid:]
# password = f"{name[:mid]}&{name[mid:]}$"
# print(password.swapcase())



# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if (x1 + y1 ) == (x2 + y2):
#     print("YES")
# else:
#     print("NO") 




# name_of_list = ['Helloworld!']
# nelist = str(name_of_list)
# new_list = list(nelist[2:-2])
# num = int(len(new_list ) / 2)

# if int(len(new_list ))%2 != 0:
#     print(new_list [(num + 1):] + new_list [:(num + 1)])
# else:
#     print(new_list [num:] + new_list [:num])





# name = input("name: ").split()
# name1 = name[0].replace("a", "")
# name2 = name[1]

# for i in name2:
#     sol = print(i + "*", end = "")
    

# suitcase = []
# suitcase.append('sfsf')
# suitcase.append('sfsfdsfdsf')
# suitcase.append('bvcfcc')
# suitcase.append('ewdscx')
# suitcase.append('dsfdsfv')
# suitcase.pop(-1)
# suitcase.insert(0, "panama")
# print(suitcase)

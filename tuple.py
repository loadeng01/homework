# tuple - кортеж - неизменяемый, индексируемый тип данных
# предназначен для хранения любых данных (в целом не отличаются от списков, просто их нельзя изменить и занимают они больше памяти)


# tup = (1, 2, 3, 43, 12, 5, "sddsaa", [8, 76, 5, 4], ("", "freak", True), False)



# tuple1 = ([1,2,3], 1, 'h', [4,5,6], '1', 2, [7,8,9])

# for i in tuple1:
#     if type(i) == list:
#         i.append(2)

# print(tuple1)


# lists = [[1, 2, 3], [], [2], [1, 4, -4], [2, 4, 6, 1, 7]]
# lists = [[1], [1], [1]]

# max_list = []
# min_list = []
# ind =[]

# for i in lists:
#     ind += [len(i)]

# check = all(x == lists[0] for x in lists)

# if len(lists) == 1:
#     max_list = []
#     min_list = None
# elif check == True:
#     max_list = lists[ind.index(max(ind))]
#     min_list = None
# else:
#     max_list = lists[ind.index(max(ind))]
#     min_list = lists[ind.index(min(ind))]
   
# print(max_list)
# print(min_list)








# словари - это из наиболее часто импользуемых структур данных, позволяющий хранить объкты
# словарь - изменяемый, итерируемый неиндексируемый тип даных 
# в котором элементы хранятся в виде пары ключ значение

# dic = {'name': 'John', 'age': 23, 'hobby':['hucking', 'pick uping']}
# dic = dict([('key1', 'value1'), ('key3', 'vallle3')])


# dict1 = dict()
# dict1["gre"] = "walue12"



# print(dic.get('key1', 'key3'))


# print(list(dic.items()))


# dic = {'awe': None, 'bed': None, 'cass': None, 'dasdsad': None}

# for key, value in dic.items():
#     dic[key] = len(key)

# print(dic)


# dic = {'John': 60, 'Jack': 70, 'Anton': 85, 'Beka': 81, 'Nastya': 93}
# ave = 0

# for value in dic.values():
#     ave += value

# ave = ave // len(dic)

# dic.update(average = ave)
# print(dic)




# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# neww = []

# for i in range(len(list_)):
#     neww += [list_[i::step]][:step]

# print(neww)


# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = [list_[i::step] for i in range(len(list_))][:step] 
# print(list1)



# size = 3
# num = []
# num += range(1, size + 1)
# num = [num] * size 

# print(num)


# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']

# word = input("W: ").lower()
# serch = []

# for i in list_:
#     if i[0] in word:
#         serch.append(i)

# print(serch)


# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]

# ave = [] 

# # for i in colors1:
# #     if i in colors2:
# #         ave += [colors1.index(i)]

# # ave[1] = ave[1] - 1
# # for i in ave:
# #     colors1.pop(i)


# # for i in colors1:
# #     if i in colors2:
# #         ave += [colors1.index(i)]


# # for i in ave:
# #     colors2.pop(i)

# for i in colors1:
#     for j in colors2:
#         if i == j:
#             colors1.remove(i)
#             colors2.remove(j)

# colors2.remove("blue")
# colors1.remove("blue")


# # print(colors1, colors2, sep="\n")

# print(colors1, colors2, sep="\n")



# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]

# check = bool

# for i in list1:
#     if i in list2 or i in list2:
#         check = True
#     else:
#         check = False

# print(check)


# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# repeats = 3
# newl = []

# for i in list_:
#     if list_.count(i) >= repeats:
#         newl += [i]


# li = []
# [li.append(x) for x in newl if x not in li]

# print(li)


# list_ = [1, 2, 3]


# from itertools import permutations 
# list_ = [1, 2, 3] 
# comb = permutations(list_) 
# for i in comb: 
#     print(i)

# k = 3
# lis = [[]] * k

# for i in lis:
#     i.append(0) 

# print(lis)


# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# clor = []
# colar = []

# for i in colors:
#     clor += [i[::-1]]

# for i in sorted(clor, key=len):
#     colar += [i]

# print(colar)

# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'A'
# newl = []

# for i in list_:
#     newl += [i]
#     newl.insert(step, element) 
#     step += 3

# print(newl)


# list_ = [1,2,3,4,5,6,7,8,9,0] 
# step = 2
# element = "A" 
# for x in list_: 
#     if step < len(list_): 
#         list_.insert(step, element) 
#         step += 3
        
# print(list_)

# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# summ =[]

# for i in lists:
#     summ += [sum(i)]

# max_val = lists[summ.index(max(summ))]

# print(max_val)





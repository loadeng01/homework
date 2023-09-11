# set() - множества, это изменяемый неупорядоченный итерируемый и не индексируемый тип данных

# хранит только уникальные значения, а так же хранят только неизмяемый тип данных

# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# repeats = []

# for i in list_:
#     if list_.count(i) >= 2:
#         repeats += [i]


# li = []
# [li.append(x) for x in repeats if x not in li]

# print(li)

# ser = set()
# ser.update([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20])
# print(ser)




merge_from = input("N: ")
merge_to = input("N: ")
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

ind1 = chars.index(merge_from)
ind2 = chars.index(merge_to) + 1
ster = "".join(chars[ind1:ind2])

newl = []
[newl.append(i) for i in chars if i not in ster]
newl.insert(ind1, ster)

print(newl)





# списки
# изменяемый тип данных, индексируемый, упорядоченный
# итерируемый тип данных


# muk = [1,2,3, 'hello', [1,2,3], {'a':3}]

# names = input("enter names with spaces: ").lower().split()
# guest = input("name: ").lower()


# mov.remove("Inception")
# print(mov)


# mov = ["Interstellar", "Pulp Function", "Inception", "Nolan", 1, 2, 3]


# nums = list(range(1, 51))
# nums1 = []
# nums2 = []


# for i in nums:
#     if i%2 != 0:
#         nums1.append(i)
#     else:
#         nums2.append(i)

# print(nums1)
# print(nums2)






# nums = input("Введите цифры через запятую: ").split(",")
# new = []

# for i in nums:
#     new.append(int(i))

# print(nums[0], nums[-1])

# new[-1] = "Makers"
# print(new)




# import random

# nums = []

# for i in range(10):
#     random_nums  = random.randint(1, 100)
#     nums += [random_nums]

# nums.sort()
# print(nums)



# text = input("Вводите слова через запятую с пробелом: ").split(", ")
# nums = []

# for i in text:
#     nums += [len(i)]

# print(text)
# print(nums)



# list_ = [-1, -124, -674, -523]
# min_number = list_[0] 
# for i in range(len(list_)): 
#     if list_[i] < min_number: 
#         min_number=list_[i] 
        
# print(min_number)


# tuples = [('Testing', 'error', 'success'), (1, 5.5, {'age': 17}), (), (), ()] 

# for i in tuples:
#     if i == ():
#         tuples.remove(i)

# tuples.remove(())

# print(tuples)

# tuples = [('Testing', 'error', 'success'), (1, 5.5, {'age': 17}), (), (), ()] 
# cleared_tuples = [c for c in tuples if c] 
# print(cleared_tuples)

# name1 = input("Name: ").split().pop()
# name2 = input("Name: ").split().pop()
# name3 = input("Name: ").split().pop()
# name4 = input("Name: ").split().pop()
# name5 = input("Name: ").split().pop()

# names = []

# names.append(name1)
# names.append(name2)
# names.append(name3)
# names.append(name4)
# names.append(name5)

# print(names)

# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# nums = [i for i in list_ if type(i) == int]
# lett = [i for i in list_ if type(i) != int]

# for i in lett:
#     if i in "123456789":
#         nums.append(int(i))

# summ = 0

# for i in nums:
#     summ += i

# print(summ)


# str_list = ['asd', 'des', 'ard', 'fresko', 'ardsdf']
# ind = []

# for i in str_list:
#     for j in str_list:
#         if i[0] == j[0] and i[-1] == j[-1]:
#             ind += [str_list.index(i)]

# nums = list(range(0, 10))

# for i in ind:
#     if i in nums:
#         ind.remove(i)

# ind.remove(3)

# print(ind)

# str_list = ['abc', 'xyz', 'aba', '1221'] 
# index = [] 
# for x in str_list: 
#     if x [0]==x[-1]: 
#         index.append(str_list.index(x)) 
        
# print(index)








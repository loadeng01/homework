# def repeat(num):
#     def decorator(func):
#         def wrapper(info):
#             for i in range(num):
#                 print(info)
#         return wrapper
#     return decorator

# @repeat(5)
# def func(name: str):
#     print(f'{name}')

# func("Peace")



# def countdown(seconds):
#     def decorator(func):
#         for i in sorted(range(1, seconds + 1), reverse=True):
#             print(i)
#         def wrapper():
#             func()
#         return wrapper
#     return decorator

# @countdown(5)
# def func():
#     print("Hello world")

# func()

# ut = dict({12:23})
# ut.fromkeys(ut)
# ut.update({125:23})
# ut['name'] = 144

# print(ut)

# lis = [*range(10)]
# hel = "hello"
# hel = ['h', 'e', 'l', 'l', 'o']

# print(divmod(10, 15))

ter = tuple([1,2,3,4,5])
tup = 1,2,3,4,5,[1,2,3,4],
rer = [1,2,3,4,5, [1,2,3]]
re = rer.copy()
# re[-1].append(990)
# print(rer)
# for i in tup:
#     print(i)

# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped
# def makeitalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped

# @makebold
# @makeitalic
# def hello():
#     return "hello world"

# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print(arg1, arg2)
#         function_to_decorate(arg1, arg2)
#     return a_wrapper_accepting_arguments


# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print("Меня зовут", first_name, last_name)
    

# print_full_name("Питер", "Венкман")


# def a():
#     if 1:
#         return 1
#     return 2

# def b():
#     return a

# print(b()())


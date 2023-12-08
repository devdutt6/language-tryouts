# Duck typing: the methods of the class is more important than attributes
# "If it walk like a duck and talk like a duck it must be duck"
# class Duck:
#     def walk(self):
#         print("duck walk")
#     def talk(self):
#         print("duck talk")
# class Cat:
#     def walk(self):
#         print("cat walk")
#     def talk(self):
#         print("cat talk")
# def catch(duck):
#     duck.walk()
#     duck.talk()
#     print("caught duck")
# catch(Duck())

# walrus operator (assigns value to variable as beign part of larger expression)
# foods = list()
# while food:=input("What food do you like? ") != "quit":
#     foods.append(food)

# function as variable
# def sum(o, s):
#     return o+s
# add = sum # same memory reference so will run the same function
# print(add(2, 3))

# higher order function
# a function either receives function as a argument or returns a function or both
# def loud(text):
#     return text.upper()
# def quiet(text):
#     return text.lower()
# def hello(fun):
#     return fun("Hello")
# print(hello(loud))
# print(hello(quiet))
# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend
# divide = divisor(2)
# print(divide(10))

# lambda function
# it is a function in one line which accepts any number of arguments and has only one expression
# double = lambda num : num * 2
# full_name = lambda f, l : f'{f} {l}'
# print(double(2))
# print(full_name(l="dutt", f="dev"))

# sort method(for list) and sort function(for iterables)
# names = ["mitesh", "meet", "abhi", "chatur"]
# names.sort()
# for i in names:
#     print(i)
# names.sort(reverse=True)
# for i in names:
#     print(i)
# function
# names = ("mitesh", "meet", "abhi", "chatur")
# sorted_names = sorted(names, reverse=True)
# for i in sorted_names:
#     print(i)
# students = [
#     ("mitesh", "A", 21),
#     ("meet", "B", 20),
#     ("abhi", "C", 19),
#     ("chatur", "D", 17),
# ]
# grade = lambda tup : tup[1]
# students.sort(key=grade)
# for i in students:
#     print(i)

# map(function, iterable)
# store = [
#     ("book", 20.00),
#     ("newspaper", 2.00),
#     ("burger", 22.00),
#     ("fries", 10.00),
# ]
# to_euro = lambda tup : (tup[0], tup[1] * 0.82)
# store_euro =  list(map(to_euro, store))
# for i in store_euro:
#     print(i)

# filter
# names = [
#     ("mitesh", 20),
#     ("meet", 2),
#     ("abhi", 22),
#     ("chatur", 10),
# ]
# isAllowed = lambda tup : tup[1] > 18
# drinking_buddies =  list(filter(isAllowed, names))
# for i in drinking_buddies:
#     print(i)

# reduce
# import functools
# names = [ 20, 2 ,22 ,10]
# add = lambda age, age2 : age + age2
# total_age = functools.reduce(add, names)
# print(total_age)

# list comprehension
# [expression for i in iterable]
# [expression for i in iterable if]
# [expression if/else for i in iterable]
# normal
# squares = []
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)
# using comprehension
# squares = [i*i for i in range(1, 11)]
# print(squares)
# students = [12, 40, 60, 66, 70, 55, 81, 90]
# passed_student = [i for i in students if i >= 60]
# passed__student = [i if i >= 60 else "FAILED" for i in students]
# print(passed_student)
# print(passed__student)

# dictionary comprehension
# {key : expression for key, value in iterable}
# {key : expression for key, value in iterable if}
# {key : expression if/else for key, value in iterable}
# city = {
#     "NY": 32,
#     "CL": 75,
#     "FL": 100,
#     "TX": 50
# }
# hot_cities = {key: round((value-32)*(5/9)) for (key, value) in city.items()}
# print(hot_cities)
# warm_city = {key: value  for (key, value) in city.items() if value > 40}
# print(warm_city)
# def check_temp(value):
#     if value >= 100:
#         return "TOO_HOT"
#     elif 50 <= value < 100:
#         return "WARM"
#     else:
#         return "COLD"
# city_read = { key: check_temp(value) for (key, value) in city.items() }
# print(city_read)

# zip(*iterables)
# names = ["dev", "dutt"]
# age = (20, 21)
# male = (True, False)
# mixer = zip(names, age, male)
# for i in mixer:
#     print(i)

# if some module is run as a main module or ran from other module indirectly
# python adds a special variable __name__ in every module and if the module is run directly then __name__ for that module be '__main__' else will be the name of the module/file
# def hello():
#     print("Hi")
# if(__name__ == "__main__"):
#     print("direct")
#     hello()
# else:
#     print("indirect")

# time module
# import time
# time strftime, strptime, local, time, ctime, asctime

# threading
# multi processing (recommended when cpu bound)
# multi threading (recommended when io bound)
# no process is truly multi threading in python due to GIL(Global Interpreter Lock)
# so they are executed turn after turns
# import threading
# import time
# def eat():
#     time.sleep(2)
#     print("ate")
# def drink():
#     time.sleep(2)
#     print("drink")
# def study():
#     time.sleep(2)
#     print("study")
# x = threading.Thread(target=eat)
# x.start()
# # x.join() # to make wait main thread for finishing the execution of x thread
# y = threading.Thread(target=drink)
# y.start()
# z = threading.Thread(target=study)
# z.start()
# print(time.perf_counter())
# print(threading.active_count())
# print(threading.enumerate())
# # eat()
# # drink()
# # study()

# daemon thread
# The main thread will not wait for daemon thread to complete its execution
# it will only wait for non daemon thread
# they are used when want to run some background task they will be killed as soon as main completes execution
# import time
# import threading
# def timer():
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("passed", count, "seconds")
# # It will continue running cause it is not a daemon thread
# # x = threading.Thread(target=timer)
# # x.start()
# # It will stop as soon as main thread gets execution completion event
# x = threading.Thread(target=timer, daemon=True)
# x.start()
# answer = input("Do you wish to continue? ")

# multiprocessing
# from multiprocessing import Process, cpu_count
# import time
# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
# if __name__ == "__main__":
#     print(cpu_count())
#     a = Process(target=counter, args=(100000000,))
#     b = Process(target=counter, args=(100000000,))
#     a.start()
#     b.start()
#     a.join()
#     b.join()
#     print(time.perf_counter())

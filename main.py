# fruits = ('banana', 'apple', 'blueberry', 'cherry')
#
# word = input('Соз жаз: ')
# if word in fruits:
#    print(word)
#
# else:
#    print('jok')
# '''
# Соз жаз: apple
# 1
#
# Соз жаз: cherry
# 3
#
# Соз жаз: melon
# jok

#
# words = 'my name is Kazybaev'
# new_words = words.split()
# n = len(new_words[-1])
# print(f'узундугу {n}')





# fruits = ['banana', 'apple', 'blueberry', 'cherry']
# we = input('name: ')
# if we in fruits:
#   fruits.remove(we)
#   print(fruits)
# else:
#     print('jok')




# name: Kyrgyzstan
# Salam
#
# name: Russia
# Privet
#
# name: USA
# Hello
#
# name: China
# Error



# li_name = input('name: ')
# if li_name == 'Kyrgyzstan':
#    print('Salam')
# elif li_name == 'Russia':
#    print('Privet')
# elif li_name == 'USA':
#    print('Hello')
# else:
#    print('Ero')
#



# cars = ['audi', 'tesla', 'bmw', 'tesla', 'tesla', 'audi']
# car = set(cars)
# ca = list(car)
# print(ca)
# ['audi', 'tesla', 'bmw']


# nums1 = {3, 4, 5, 2}
# nums2 = {5, 2, 4, 9}
#
# nu1 = tuple(nums1)
# nu2 = tuple(nums2)
#
# nol = nu1 + nu2
# nol = (sorted(nol, reverse=True))
#
# print(nol)
# (9, 5, 5, 4, 4, 3, 2)



# окшош машиналар 3




#
# cars1 = ['tesla', 'bmw', 'audi', 'honda']
# cars2 = ['mers', 'bmw', 'byd', 'audi', 'honda']
#
# car1 = set(cars1)
# car2 = set(cars2)
#
# no = car1.intersection(car2)
#
# n = len(no)
#
# print(f'окшош машиналар {n}')





# person = {'first_name': 'Aelita', 'age': 16, 'country': 'Kg'}
#
# word = input('write a key: ')
#
# if word in person:
#  print(person.get(word))
# else:
#  print('jok')




'''
# write a key: age
# 22
#
# write a key: name
# jok
#
# write a key: country
# KZ
'''




# person = {'first_name': 'Aelita', 'age': 16, 'country': 'Kg'}
#
# word = input('write a key: ')
#
# if word in person:
#     print(person[word])
# else:
#     print('Jok')





# try:
#     numbers1 = (4, 5, 6, 2, 7)
#     numbers2 = (7, 8, 6, 0, 1)
#
#     num2 = set(numbers2)
#     num1 = set(numbers1)
#
#     dol = num2.difference(num1)
#
#     print(dol)
#
# except NameError:
#     print('Код туура эмес')
# finally:
#     print('Код иштеп бутту')

# (8, 0, 1)





# cars = ['honda', 'tesla', 'mers', 'tiko']
#
# i = element = input('name: ')
# r = numbers = int(input('index: '))
#
# cars.insert(r, i)
#
# print(cars)






#
# # '''
# : Laptop
# San: 0
# [Laptop, 'honda', 'tesla', 'mers', 'tiko']
#
# : phone
# San: 3
# ['honda', 'tesla', 'mers',phone,  'tiko']
#
#


#
# fruits = ['apple', 'banana', 'cherry', 'melon']
#
# for n in fruits:
#     print(len(n))
'''#5
#6
#6
#5
'''
#
# long = input('name :')
# for goin in long:
#     print(goin)

# name = input('name : ')
# age = int(input('index : '))
#
# for i in range(age):
#     print(name)

# numbers = [6, 7, 3, 8, 3]
#
# for i in reversed(numbers):
#
#     print(i*10)
#30
#80
#30
#70
#60

# numbers = [6, -7, -3, -8, 3]
#
# for n in numbers:
#
#  if n > 0:
#      print(n)
#

#6
#3

# nums = [5, -2, 3, -7, -3, 8]
# total_list = []
# for k in nums:
#     if k > 0:
#         total_list.append(k)
#     elif k < 0:
#         total_list.append(0)
# print(total_list)

# [5, 0, 3, 0, 0, 8]


# numbers = [5, 6, 8, 10, 3, 15]
# new_list = []
# for i in numbers:
#     if i % 5 == 0:
#         new_list.append(i)
# print(new_list)



#[5, 10, 15]

# oli = int(input('numbers..: '))
# print('start')
# while oli > -1:
#
#
#     print(oli)
#     oli -= 1
# print('fro')

# number2 = int(input('2 san: '))
#
# for i in range(number1, number2+1):
#     print(i)



# nums = {4, -5, 1, -6, -8}
# total_list = set()
# for k in nums:
#     if k > 0:
#         total_list.add(k*2)
#     elif k < 0:
#         total_list.add(k*10)
# print(total_list)
#{8, -50, 2, -60, -80}






# nums = int(input('san : '))
#
#
# for i in range(1, 11):
#     print(i, '*', nums, "=", i * nums)

# def numbers(nums):
#     new_list = []
#     for i in nums:
#         new_list.append(i * 2)
#     return new_list
# print(numbers([5,3,5,2,56]))

# 10, 6, 10, 4, 112

# def form_list(a,i):
#  nol_list = [a,i]
#
#  return nol_list
#
#
# print(form_list('Marlen', 'Bishkek'))


# ['Marlen', 'Bishkek']


# def form_list(name, city):
#     new_list = []
#     new_list.append(name)
#     new_list.append(city)
#     return new_list
#
# print(form_list('Marlen', 'Bishkek'))


# ['Marlen', 'Bishkek']

# def new_cars(car):
#     nol_on = []
#     for i in car:
#         if i == 'tesla':
#             nol_on.append(i)
#
#     return nol_on
#
#
#
#
#
# print(new_cars(['bmw', 'tesla', 'audu', 'tesla', 'tesla']))
# ['tesla', 'tesla', 'tesla']



# def two_lists(i,r):
#
#     total = i + r
#     v = sorted(total, reverse=True)
#
#     return v
#
#
# print(two_lists([4, 3, 1], [8, 2, 6]))


# [8, 6, 4, 3, 2, 1]


# def unique_numbers(num1,num2):
#     nums1 = set(num1)
#     nums2 = set(num2)
#     tong = nums1.union(nums2)
#     class_list = list(tong)
#     return sorted(class_list, reverse=False)
#
#
#
# print(unique_numbers([5, 6, 2, 7], [5, 6, 2, 3]))


# [2, 3, 5, 6, 7]



# def check_number(number):
#     if number > 0:
#         return '+ san'
#     else:
#         return '- san'
#
# print(check_number(-8))
#



# check = lambda number: print('+san') if number >  0 else print('-san')
# check(-87)

# def unique_numbers(a, b):
#     a.extend(b)
#     new_a = set(a)
#     return sorted(new_a)
#
# print(unique_numbers([5, 6, 2, 7], [5, 6, 2, 3]))

# def change_numbers(words, key):
#     if key in words:
#         return words[key]
#     else:
#         return 'Jok'
#
# print(change_numbers({'name': 'Acer', 'price': 5000}, 'name'))

#age
#jok


#price
#5000

# def check_words(word,long):
#
#       if word == long[:: -1]:
#           return 'palindrom'
#       else:
#           return ' palindrom emes'
#
# print(check_words('re','rer'))

# ata   ata == ata
# palindrom
#
# car car == rac
# palindrom emes

# def two_sums(g, j):
#     return g + j
#
# print(two_sums(3,5))
#
# a = lambda g, j: g + j
# print(a(6, 7))

#
# def check_number(number):
#     for i in range(number):
#         print(i)
#
# check = lambda a: [print(i) for i in range(a)]
# check(7)

#
# print_word = lambda word, number: [print(word) for i in range(number)]
# print_word('uweihyweiur', 3)




#laptop
#laptop
#laptop





# new_numbers = lambda a :[print(i*5) for i in range(1,a+1)]
#
# new_numbers(3)



# 5
# 10# 15
# def check_age(a):
#     # for a in range(check_age):
#         if a >18 :
#          print('chon')
#         elif a <18 :
#             print('kichi')

#
# check_age(43)

# check_age = lambda a : print('chon') if a > 18 else print('kichi')
# print('kichi')
# elif a <18:
# check_age(43)

# def check_number(nard):
#     if nard % 2 == 0:
#         return 'jup san'
#     elif nard % 2 > 0:
#         return 'tak san'
#
#
# print(check_number(10))







#                                                class             ООП





# class Comp:
#     def __init__(self, name, price, storege, ram, cpu):
#         self.name = name
#         self.price = price
#         self.storege = storege
#         self.ram = ram
#         self.cpu = cpu
#
#     def show(self):
#         return f'{self.name},{self.price},{self.storege},{self.ram},{self.cpu}'
#
# comp1 = Comp('lenovo','core i5','8gb oper','red','1000/700')
#
# print(comp1.show())
# class Laptop:
#     def __init__(self, name, price, storege, ram, cpu):
#
#        self.name = name
#        self.price = price
#        self.storege = storege
#        self.ram = ram
#        self.cpu = cpu
#     def show(self):
#         return f'{self.name},{self.price},{self.storege},{self.ram},{self.cpu}'
#
# nout1 = Laptop('macbook pro 15','220000','16gb oper','m3','1000/700')
#
# print(nout1.show())
#


# class Shape:
#     def __init__(self, a):
#         self.a = a
#     def perimetr(self):
#          pass
# class Circle(Shape):
#     def __init__(self, a):
#         super().__init__(a)
#     def Perimetr(self):
#         return (self.a + 2) * 3
# class Rectangle(Circle):
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.b = b
#     def perimetr(self):
#         return (self.a + self.b) * 2
# rek1 = Rectangle(4, 5)
# print(f'sm...', rek1.Perimetr())
# class Triangle(Rectangle):
#
#     def __init__(self, a, b, c):
#         super().__init__(a, b,)
#         self.c = c
#     def perimetr(self):
#
#          return (self.a * self.b * self.c)
# tr1 = Triangle(4, 5, 8)
# print(tr1.perimetr())

#                                           кайталоооо



#
# nums1 = [4, 3, 5, 7]
# nums2 = [5, 3, 6, 9]
#
# num1 = set(nums1)
# num2 = set(nums2)
#
# long = num2.difference(num1)
# lonch = list(long)
# print(lonch)  
# [6, 9]



# numbers = [4, 6, 3, 7, -5, 2, 8]
# nol = []
#
# for i in numbers:
#     if i > 5:
#        nol.append(i)
#
# moin = tuple(nol)
# print(moin)
#(6, 7, 8)


# nums = [7, 76, 43, 23, 65]
# max_number = 0
# for i in nums:
#     if max_number < i:
#         max_number = i
# print(f'max number is ', max_number)
#


# max number is 76


#
#
#
# laptops = [
#     {
#         "name": 'Macbook',
#         "price": 125000,
#         "color": "Silver"
#     },
#     {
#         "name": 'Asus',
#         "price": 34000,
#         "color": "Black"
#     },
#     {
#         "name": 'Acer',
#         "price": 67000,
#         "color": "White"
#     },
# ]
#
#
# for i in laptops:
#     new_list = list(i)
#




# def find_index(func, pes):
#     nol_on = []
#     for i in func.index(pes.index):
#         if i + i = pes:
#             nol_on.append(i)
#
#     return nol_on
#


#


#[5, 6, 1, 4], 10
# [1, 3]

# [5, 6, 1, 4], 9
# [0, 3]

#[5, 6, 1, 4], 15
# []

# find_index = [5, 6, 1, 4]
# nums = input('number: ')
# def fucnk()
# for i in find_index:
#     if i == nums in find_index:
#
#         print(i)


# name = input('name : ')
# age = int(input('index : '))
#
# for i in range(age):
#     print(name)

# numbers = [6, 7, 3, 8, 3]
#
# for i in reversed(numbers):


#
#
# def find_index(find, index):
#     new_list = []
#     for i in range(len(find)):
#         for a in range(i + 1, len(find)):
#             if find[i] + find[a] == index:
#                 new_list.append(i)
#                 new_list.append(a)
#     return new_list
#
# print(find_index([5, 5, 2, 7], 10))
# #

#
# user = [5, 1, 9, 7]
# target = 10
#
# res = []
# for i, e in enumerate(user):
#     t = target - e
#     if t in user:
#         if not res:
#             res.append(user.index(e))
#         elif res[0] == user.index(e) and user.count(e) > 1:
#             res.append(user[::-1].index(e))
#         # else:
#         #     continue
#     print(user.count(e))
#     if len(res) == 2:
#         break
# print(res)


#
#
# user = [5, 1, 9, 7]
# target = 10
#
# res = []
# for i, e in enumerate(user):
#     t = target - e
#     if t in user:
#         if target / 2 == t and user.count(e) == 2:
#             res.append(user.index(e))
#             a = user
#             res.append(a.remove(e).index(t))
#         elif t in user and e in user:
#             res.append(user.index(e))
#             res.append(user.index(t))
#         # elif res[0] == user.index(e) and user.count(e) > 1:
#         #     res.append(user[::-1].index(e))
#         # else:
#         #     continue
#     # print(user.count(e))
#     if len(res) == 2:
#         break
# print(res)

#
# laptops = ('Macbook', 'Asus', None, 'Acer', None)

# print(laptops.count(None))

#
# for i in laptops:
#     if i is None:
#         print(i)





# #
# cars = [
#     {
#         'name': 'Audi',
#         'price': 45000
#     },
#     {
#         'name': 'Tesla',
#         'price': 56000
#     },
#     {
#         'name': None,
#         'price': 34000
#     },
#     {
#         'name': None,
#         'price': 45000
#     },
#     {
#         'name': 'Mers',
#         'price': 78000
#     },
# ]
#
#
#
# for i in cars:
#     # if i['name'] is None:
#      i['price'] = 1000
#      print(i)



#
# for i in cars:
#     if i['name'] is None:
#         print(True)
#     else:
#         print(False)








# True
# True
# False
# False
# True





# def check_list(dela):
#     free = set(dela)
#     for i in free:
#         if i in free:
#             return True
#         elif i + i:
#             return False
# print(check_list([4, 6, 7, 7]))
# True

#print(check_list([4, 6, 7, 7]))
# False

# def check_list(numbers):
#     check_list(set(numbers))
#     if numbers == check_list:
#         return True
#     return False
# print(check_list([4, 6, 7, 7]))


# def check_list(numbers):
#     fff = set(numbers)
#     if len(fff) == len(numbers):
#         return True
#     return False
#
#
# print(check_list([3, 5, 2, 4]))


# def check_list(werds, name):
#     try:
#         werds.remove(name)
#         return werds
#     except ValueError:
#         return 'Андай машина жок'
#     except TypeError:
#         return 'list jaz'

#
# def check_list(words, name):
#     try:
#         words.pop(name)
#         return words
#     except IndexError:
#         return 'Андай index жок'
#
# cars = ['Audi', 'Mers', 'Honda', 'Tiko', 'Bmw']


# print(check_list(cars, -3))
# ['Audi', 'Mers', 'Tiko', 'Bmw']

# print(check_list(cars, 10))
# Андай машина жок



# def change_numbers(numbers):
#     try:
#         new_list = []
#         for a in numbers:
#             if a > 0:
#                 new_list.append(a)
#             elif a < 0:
#                 new_list.append(0)
#         return new_list
#
#     except TypeError:
#         return 'list jaz'
#     except NameError:
#         return 'az jaz'

# print(change_numbers([4, 5, -3, -6, 7]))


# [4, 5, 0, 0, 7]

# def change_value(list_value, key, number):
#     try:
#         for i in list_value:
#             i[key] = i[key] - number
#             print(i)
#     except TypeError:
#         print('Аргумен dict болсун')
#     except KeyError:
#         print('Ключ туура эмес')
#     except NameError:
#         print('Код туура эмес')
#     finally:
#         print('Код иштеп бутту')
#
#
#
# cars = [
#     {
#         'name': 'Audi',
#         'price': 45000
#     },
#     {
#         'name': 'Tesla',
#         'price': 56000
#     },
#     {
#         'name': 'Honda',
#         'price': 45000
#     },
#     {
#         'name': 'Mers',
#         'price': 78000
#     },
# ]
#
# change_value(cars, 'price', 5000)


# ////////////////////////////////////////////////////////////////////



# try:
#     numbers1 = (4, 5, 6, 2, 7)
#     numbers2 = (7, 8, 6, 0, 1)
#
#     num2 = set(numbers2)
#     num1 = set(numbers1)
#
#     dol = num2.difference(num1)
#
#     print(dol)
#
# except NameError:
#     print('Код туура эмес')
# finally:
#     print('Код иштеп бутту')


#
# try:
#     def numbers(nums):
#         new_list = []
#         for i in nums:
#             new_list.append(i * 2)
#         return new_list
#
#     print(numbers([5, 3, 5, 2, 56]))
#
# except TypeError:
#     print('Аргумен dict болсун')
# except NameError:
#     print('Код туура эмес')
# finally:
#     print('Код иштеп бутту')



# try:
#     def check_words(word, long):
#
#         if word == long[:: -1]:
#             return 'palindrom'
#         else:
#             return 'palindrom emes'
#
#
#     print(check_words('rer', 'rer'))
#
# except TypeError:
#     print('Аргумен dict болсун')
# except NameError:
#     print('Код туура эмес')
# finally:
#     print('Код иштеп бутту')
#














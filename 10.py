# #1
# import random
#
# class Simple:
#
#     def __init__(self, digit_a: int, digit_b: int):
#         self.digit_a = digit_a
#         self.digit_b = digit_b
#
#     def output(self):
#         print(self.digit_a, self.digit_b)
#
#     def randomer(self):
#         self.digit_a = random.randint(1, 10)
#         self.digit_b = random.randint(1, 10)
#         print(self.digit_a, self.digit_b)
#     def summ(self):
#         print(self.digit_a + self.digit_b)
#
#     def maximum(self):
#         if self.digit_a > self.digit_b:
#             print(self.digit_a)
#         else:
#             print(self.digit_b)
#
#
# Digit = Simple(2,5)
# Digit.summ()
# Digit.output()
# Digit.maximum()
# Digit.randomer()

# # 2
# class Counter:
#     current = 0
#
#     def __init__(self, start=1, end=10):
#         self.start = start
#         self.end = end
#
#     def info(self):
#         print(self.current)
#
#     def increase(self):
#         if self.current < self.end:
#             self.current += 1
#             print(self.current)
#             return self.current
#         else:
#             return print("Vixod za granici")
#
#     def crease(self):
#         if self.current > self.start:
#             self.current -= 1
#             print(self.current)
#             return self.current
#         else:
#             return print("Vixod za granici")
#
#
# Sekund = Counter(0, 3)
#
# Sekund.increase()
# Sekund.increase()
# Sekund.increase()
# Sekund.crease()
# Sekund.increase()
# Sekund.info()

# # 3
# class Shop:
#     dct = {}
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.add(self.name)
#
#
#     def add(self, name):
#         if name in self.dct.keys():
#             print("Такой товар уже есть в магазине!")
#
#         else:
#             self.dct[self.name] = self.price
#
#     def dele(self):
#         if self.name in self.dct.keys():
#             del self.dct[self.name]
#             self.info()
#         else:
#             print("Такой товар отсутствует в магазине!")
#
#     def search(self):
#         if self.name in self.dct.keys():
#             print(self.dct[self.name])
#         else:
#             print("Такой товар отсутствует в магазине!")
#
#     def info(self):
#         print(self.dct)
#
#
# Apple = Shop("Apple", 2.45)
# Tomato = Shop("Tomato", 4.65)
# Potato = Shop("Potato", 1.15)
# Cucumber = Shop("Cucumber", 5.25)
# Carrot = Shop("Carrot", 2.1)
# Carrot.dele()
# Potato.search()

# # 4
# class MoneyBox:
#     count_money = 0
#
#     def __init__(self, capacity):  # конструктор с аргументом- вместимость копилки
#         self.capacity = capacity
#
#     def can_add(self, v):  # True, если можно добавить v монет, False иначе
#         if self.count_money + v > self.capacity:
#             return False
#         else:
#             return True
#
#     def add(self, v):  # положить v монет в копилку
#         if self.can_add(v):
#             self.count_money += v
#             self.info()
#         else:
#             print("UNKNOW 404")
#
#     def info(self):
#         print(self.count_money)
#
# Svinnya=MoneyBox(10)
# Svinnya.add(3)
# Svinnya.add(3)
# Svinnya.add(3)
# Svinnya.add(1)
# Svinnya.add(3)



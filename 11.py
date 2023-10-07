##1
# class ChessPiece:
#     def __init__(self, x, y, color):
#         self.x = x
#         self.y = y
#         self.color = color
#
#     def can_beat(self, x, y):
#         pass
#
#
# class Queen(ChessPiece):
#     def can_beat(self, x, y):
#         return self.x == x or self.y == y or abs(self.x - x) == abs(self.y - y)
#
#
# class Pawn(ChessPiece):
#     def can_beat(self, x, y):
#         if self.color == 'white':
#             return self.x - x == 1 and abs(self.y - y) == 1
#         else:
#             return x - self.x == 1 and abs(self.y - y) == 1
#
#
# class Knight(ChessPiece):
#     def can_beat(self, x, y):
#         return (abs(self.x - x) == 2 and abs(self.y - y) == 1) or (abs(self.x - x) == 1 and abs(self.y - y) == 2)
# """
#
# 81 82 83 84 85 86 87 88
# 71 72 73 74 75 76 77 78
# 61 62 63 64 65 66 67 68
# 51 52 53 54 55 56 57 58
# 41 42 43 44 45 46 47 48
# 31 32 33 34 35 36 37 38
# 21 22 23 24 25 26 27 28
# 11 12 13 14 15 16 17 18
#
# """
# queen = Queen(4, 4, 'white')
# pawn = Pawn(2, 2, 'black')
# knight = Knight(3, 3, 'white')
#
# # Проверяем, может ли ферзь "бить" пешку
# print(queen.can_beat(pawn.x, pawn.y))  # Выведет True
#
# # Проверяем, может ли пешка "бить" коня
# print(pawn.can_beat(knight.x, knight.y))  # Выведет False
#
# # Проверяем, может ли конь "бить" ферзя
# print(knight.can_beat(queen.x, queen.y))  # Выведет True

# #2
# import csv
# from math import radians, sin, cos, sqrt, atan2
#
# class Carrier:
#     def __init__(self, town_1, town_2):
#         self.town_1 = town_1
#         self.town_2 = town_2
#         self.coord_1 = self.get_coordinates(town_1)
#         self.coord_2 = self.get_coordinates(town_2)
#
#     @staticmethod
#     def get_coordinates(town):
#         with open("cities.csv", "r", newline="") as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 if row["city"] == town:
#                     return [float(row["lat"]), float(row["lng"])]
#
#     def calculate_distance(self):
#         # радиус земли в километрах
#         R = 6371.0
#         lat1, lon1, lat2, lon2 = map(radians, self.coord_1 + self.coord_2)
#         dlon = lon2 - lon1
#         dlat = lat2 - lat1
#         a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
#         c = 2 * atan2(sqrt(a), sqrt(1 - a))
#         distance = R * c
#         return distance
#
#     def _cost(self, cost_in_hour, speed):
#         size_km = self.calculate_distance()
#         time = size_km / speed
#         cost = time * cost_in_hour
#         return size_km, cost, time
#
# class Plane(Carrier):
#     def cost_plane(self):
#         lst = list(self._cost(100, 900))
#         print(f'Между {self.town_1} и {self.town_2} {round(lst[0], 1)} км стоила доставка самолетом {round(lst[1], 2)}$ и заняла {round(lst[2], 1)} часов')
#
# class Car(Carrier):
#     def cost_car(self):
#         lst = list(self._cost(30, 100))
#         print(f'Между {self.town_1} и {self.town_2} {round(lst[0], 1)} км стоила доставка автомобилем {round(lst[1], 2)}$ и заняла {round(lst[2], 1)} часов')
#
# class Track(Carrier):
#     def cost_track(self):
#         lst = list(self._cost(18, 70))
#         print(f'Между {self.town_1} и {self.town_2} {round(lst[0], 1)} км стоила доставка грузовиком {round(lst[1], 2)}$ и заняла {round(lst[2], 1)} часов')
#
# fl = Plane("Minsk", "Kyoto")
# fl.cost_plane()

# # 3
# class Living:
#     def __init__(self, max_age, food=None):
#         self.age = 0
#         self.max_age = max_age
#         self.food = food
#
#     def eat(self):
#         if self.food:
#             self.food = self.food - 1
#
#     def is_alive(self):
#         if self.age >= self.max_age or (self.food is not None and self.food <= 0):
#             return False
#         else:
#             return True
#
#     def grow_older(self):
#         self.age += 1
#
#         super().__init__(max_age, food)
#
#
# class Rabbit(Living):
#     def __init__(self, max_age, food=None):
#         super().__init__(max_age, food)
#
#
# class Plant(Living):
#     def __init__(self, max_age):
#         super().__init__(max_age)
#
#
# fox = Fox(10, 5)
# fox.eat()
# fox.grow_older()
# print(fox.is_alive())  # True

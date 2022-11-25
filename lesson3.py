# class #
# моносостояние #

# class Car:
#     _property_cars = {
#         "model": "vaz",
#         "color": "blue"
#     }
#
#     def __init__(self):
#         self.__dict__ = Car._property_cars
#
#
# car1 = Car()
# car2 = Car()
# car1.model = "bmw"
# print(car2.__dict__)
# print(car1.__dict__)
# print(car1.model)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         if isinstance(other, Point):
#             return self.x == other.x and self.y == other.y
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
#
# point1 = Point(12, 6)
# point2 = Point(12, 6)
# print(point1 == point2)
# print(point1.__hash__())

# users = {}
#
# class RegisterMixin:
#     def validate_username(self):
#         if self.username in users.keys():
#             print("Такой пользователь уже существует")
#             return False
#         return True
#
#
# class Register(RegisterMixin):
#     def __init__(self, name, age, username):
#         self.name = name
#         self.age = age
#         self.username = username
#
#     def save_to_dict(self):
#         users.update({
#             self.username: {
#                 "name": self.name,
#                 "age": self.age
#             }})
#
#     def save_in_validated_data(self):
#         if self.validate_username():
#             self.save_to_dict()
#             return "saved"
#         return "did not saved"
#
# arsen = Register("Arsen", 17, "aabesov")
# print(arsen.save_in_validated_data())
# chyngyz = Register("Chyngyz", 20, "chika")
# print(chyngyz.save_in_validated_data())
# syimyk = Register("Syimyk", 18, "aabesov")
# print(syimyk.save_in_validated_data())
# print(users)

# class Investment:
#     def __init__(self, principal, interest):
#         self.principal = principal
#         self.interest = interest
#
#
#     def value_after(self):
#         print(self.principal * (1 + self.interest))
#
#     def __str__(self):
#         print(f'principal - {self.principal}, intereset - {self.interest}')
#
#
# arsen = Investment(10000, 0.5)
# arsen.value_after()
# arsen.__str__()


# class Product:
#     def __init__(self, name, amount, price):
#         self.name = name
#         self.amount = amount
#         self.price = price
#
#     def get_price(self, items):
#         self.items = items
#         if self.items < 10:
#             print(self.items * self.price)
#         if 10 < self.items < 99:
#             print((self.items * self.price) * 90 / 100)
#         if self.items >= 100:
#             print((self.items * self.price) * 80 / 100)
#         self.make_purchase()
#
#     def make_purchase(self):
#         return self.amount - self.items
#
# arsen = Product("Asu", 55, 30)
# arsen.get_price(50)
# print(arsen.make_purchase())

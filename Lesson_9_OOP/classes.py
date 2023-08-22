# class Figure:
#
#     def __init__(self, length_measurement):
#         self.length_measurement = length_measurement.upper()  # Атрибуты класса
#
#     def get_square(self):
#         pass
#
#     def get_perimeter(self):
#         pass
#
#
# class Square(Figure):  # Наследуем все что есть в фигуре в нашем квадрате. Мы наследуемся от предка Фигура.
#
#     def __init__(self, side, length_measurement):
#         super().__init__(length_measurement)
#         self.side = side  # Атрибуты класса
#         # self.measurement = measurement  # Атрибуты класса
#
#     def get_square(self):
#         return self.side ** 2
#
#     def get_perimeter(self):
#         return self.side ** 4
#
#     def __str__(self):
#         return f"side - {self.side}{self.length_measurement}"
#
#
# square = Square(5, "sm")
# # square2 = Square(456, "km")
# print(square.get_square())
# print(square.get_perimeter())
# print(f"{square.side}{square.length_measurement}")
# # print(f"{square2.side}{square2.length_measurement}")
# # print(square1 == square2)
# # square1.side = 10
# # print(square1.side)
# # print(square2.side)

class Animals():

    def __init__(self, heads_count, paw_count):
        self.heads_count = heads_count
        self.paw_count = paw_count

    def get_a_battle_roar(self):
        pass

    def bite(self):
        pass


class Cat(Animals):

    def __init__(self, heads_count, paw_count, tail, claws, cat_name):
        super().__init__(heads_count, paw_count)
        self.tail = tail
        self.claws = claws
        self.cat_name = cat_name

    def get_a_battle_roar(self):
        print("MEEOW!")

    def bite(self):
        print(f"Cat {self.cat_name} with {self.tail} is doing a KUS")


class Dog(Animals):

    def __init__(self, heads_count, paw_count, tail, claws, dog_name):
        super().__init__(heads_count, paw_count)
        self.tail = tail
        self.claws = claws
        self.dog_name = dog_name

    def get_a_battle_roar(self):
        print("GUUF!")

    def bite(self):
        print(f"Dog {self.dog_name} with {self.tail} is doing a KUS")


murzik = Cat(heads_count=1, paw_count=4, tail="Big tail", claws=18, cat_name="Murzik")
bark = Dog(heads_count=1, paw_count=4, tail="Small tail", claws=14, dog_name="Bark")
murzik.bite()
bark.bite()


list_of_animals = [murzik, bark]
for animal in list_of_animals:
    animal.bite()
# __slots__ список в котором создаем переменные в виде стринги
income_data = {"name": "sole", "species": "Betel-soul"}


class Lesson_Slots:
    __slots__ = ['instance_var', 'x', 'y']  # ограничены только слотом
    z = 10

    def __init__(self, instance_var, x, y):
        self.instance_var = instance_var
        self.x = x
        self.y = y


lesson_slots = Lesson_Slots(10, 20, 30)
print(lesson_slots.x, lesson_slots.y, lesson_slots.z)

pass

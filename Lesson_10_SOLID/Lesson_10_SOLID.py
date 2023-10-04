def get_sum(first_num, second_num):
    result = first_num + second_num
    print(result)


get_sum(1, 3)


# S.O.L.I.D - набор принципов Обтьектно ориентированого програмирования.
# Для того что бы наш код можно было переиспользывать, что бы он поддерживался.
# To create understandable, readable, and testable code that many developers can collaboratively work on
#  І на останок: Роберта Мартіна вважають Rock Star у розробці програмного забезпечення.
#  На його книгах вже виросло декілька поколінь суперуспішних програмістів.
#  «Clean Code» і «Clean Coder» — дві його книги про те, як писати якісний код і відповідати найвищим стандартам в індустрії

# DRY - Don't repeat yourself
# YAGNI - You an't gonna need it
# KISS - Keep it simple, stupid


# 1 Principle
# The Single Responsibility Principle
# Single Responsibility Principle asks us not to add additional responsibilities to a class so that we don’t have to modify a class
# unless there is change to its primary responsibility. We can handle the current situation by having separate classes that would
# handle database persistence and saving to file. We can pass the TelephoneDirectory object to the objects of those classes and
# write any additional features in those classes.

class monster_crusher():

    def __init__(self, damage_monsters):
        self.damage_monsters = damage_monsters



class fire_monster_damage(monster_crusher):

    def burn_monsters(self):
        print("Monster is burned")


class ice_monster_damage(monster_crusher):

    def freeze_monters(self):
        print("Monster is frozen")

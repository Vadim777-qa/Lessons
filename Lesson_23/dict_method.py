# hasattr()
# getattr()
# setattr()

income_data = {"name": "sole", "species": "Betel-soul"}  # json or dictionary


class Lesson23():
    class_var = 10

    def __init__(self, **kwargs):
        # kwargs is dictionary
        # self.__dict__
        self.__dict__.update(kwargs)  # instance attribute creation
        self.instance_var = 11


# # Check if an instance of Lesson23 has the "class_var" attribute
# print(hasattr(Lesson23(), "class_var"))  # This will display True
#
# # Check if the Lesson23 class has the "instance_var" attribute
# print(hasattr(Lesson23, "instance_var"))
#
# # Receive a desired attribute from the class
# print(getattr(Lesson23(), "class_var"))  # --> 10
#
# # Add a desired attribute to your class
# setattr(Lesson23, "run", lambda self: print("Check if set is working"))  # --> Check if set is working

lesson = Lesson23(**income_data, x=10, y=20)  # (name = "sole", species = "Betel-soul")
lesson.run()

for key in income_data:
    setattr(lesson, key, income_data[key])

print(Lesson23.__dict__)  # All attributes of every new class are placed in a box named __dict__ method
print(lesson.__dict__)  # Attributes that placed in an instance of this class
pass

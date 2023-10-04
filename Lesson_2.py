#  print("Vadim" in "Name is Vadim")
# test_string_procent = "Name is Vadim, age is %s"
# test_string_format = "Name is Vadim, age is {}, lived in {}"
# test_string = "Name is Vadim, age is "
# # print(test_string.upper())
# # print(test_string.lower())
# # #012345
# # print(test_string.startswith("Name", 0))
# # print(test_string.endswith("Vadim"))
#
# # print(test_string + str(27))
# #
# # procent_result = test_string_procent % 27
# # print(procent_result)
# #
# # format_result = test_string_format.format(27, "Poltava")
# # print(format_result)
#
# my_age = 30
# test_string_fstring = f"Name is Vadim, age is {my_age}, {'something'}, {True}" #буде не строка и пайтон буде использватся F string
# test_string_fstring = f"Name is Vadim, age is {my_age}, {40 - 29}, {True}"
# print(test_string_fstring)
#
# print(test_string_fstring.title())
# print(test_string_fstring.capitalize())
# print(test_string_fstring.count("i"))
# print(test_string_fstring.count('Name'))
#
#
# string_length_example = len(test_string_fstring)
# print(f'Symbols count: {string_length_example}')
# print(test_string_fstring.find('Name', 4, 10))
#
# int_str = "123"
# str_str = "asd "
# alnum_str = "asd1"
# print(int_str.isnumeric())
# print(str_str.isalpha())
# print(alnum_str.isalnum())


# test_str = "123456789"
# print(test_str[0])
# print(test_str[4])
# print(test_str[3])
# print(test_str[1:4]) # Slicing строк вирез между 1ей и 4м индексом
# print(test_str[0:6])
# print(test_str[2:7:2])
# print(test_str[-8:-1:2])

# print('New' in 'New name is Leasha')
# print(False - 1)
# print(True + True)
# print('Female don\'t cry')
# check_bool = 5 <= 5
# print(check_bool)
# concatenation = 'Pool' + ' ' + "Human"
# print(concatenation)
# check_name = "There is a big chance that people are aliens"
#
# print(check_name.upper())
# print(check_name.lower())
# print(check_name.startswith('There'))
# print(check_name.endswith('aliens'))
# print(check_name.startswith("is", 6))
#
# other_data_type = 890
# another_data_type = "110"
#
# print(type(other_data_type), type(another_data_type))
# print(other_data_type + int(another_data_type))  # conversion of types

# middle_value = "There are %s miles left to the next Region"
# after_value = "and age of the driver is %s, so don't worry"
# result_middle_value = middle_value % 35
# result_after_value = after_value % 66
# print(result_middle_value + ' ' + result_after_value)

# middle_value_format = """There are {miles} miles left to the next Region,
# and age of the driver is {age}, so don't worry"""
# format_result = middle_value_format.format(miles=35, age=66)
# print(format_result)
#
# amount_of_bunnies = 5 ** 5
# test_f_string = f"Oh my gush! There are {amount_of_bunnies}, bunnies"
# print(test_f_string.capitalize())
# print(test_f_string.title())
# print(test_f_string.count('e'))
# print(test_f_string.isalpha())
# print(test_f_string.isalnum())
# print(test_f_string.isnumeric())

# print(f'symbols count: {len(test_f_string)}')

some_str = "rt468"
print(some_str[-4:-1])

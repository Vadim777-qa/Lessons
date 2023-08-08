# def sum():
#     first_num = input("enter first num: ")
#     second_num = input("enter second num: ")
#
#     if first_num > second_num:
#         return 1
#     else:
#         return None
#
#
# sum_resut = sum()
# print(sum_resut)
#
# sum_result = sum()
# print(sum_result)


# arguments or parameters, args and kwargs (Позиционные аргументы, Key word аргумент Kwargs, )
def get_sum_of_three_numbers(first_number, second_nuber, third_number=10):
    result = first_number + second_nuber + third_number
    return result


sum_result = get_sum_of_three_numbers(4, 4, 80)
print(sum_result)

# ссілочнім типом памяти на общую ячейку памяти
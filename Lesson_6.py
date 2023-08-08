# lambda and recursive functions


var_not_in_function = 1


# can use variable out of function but can't change it
# use global hot key to change variable inside the function and then call it

def sum_two_numbers(first_number: int, second_number: int | float) -> int:  # note what do you expect from parameters
    '''

    :param first_number:
    :param second_number:
    :return:
    '''
    return first_number + second_number


# print(sum_two_numbers(1, 5))
# input_example = input("Enter name: ")
# example_string = "Alex"
# result = f"Word {input_example} has {len(input_example)} letters"
# print(result)

# first_num = int(input("Enter first number: "))
# second_num = int(input("Enter second number: "))


#Python Conditions and If statements
# if first_num > second_num:
#     print(True)
# elif first_num < second_num:
#     print(False)
# else:
#     print("Equal")

PASS_1 = input("Print your password: ")
PASS_2 = input("Confirm your password: ")

if type(PASS_1) == str and type(PASS_2) == str:
    if PASS_1 == PASS_2:
        print("Passed!")
    else:
        print("Denied!")
else:
    print("Not a name!")

# Lists (as arrays in other languages) name = []

# list_int = [1, 2, 3]
# list_string = ["Apple", "Banana"]
# list_mixed = ["Apple", 1, "Cherry"]
# print(list_mixed[1])
# list_mixed[1] = "Banana"
# print(list_mixed[1])
# print(list_int[1:3])


# # Dictionary value - Dictionaries are used to store data values in key:value pairs.
# employee_dict = {"testmail@hs.com": "Test Employee 1",
#                  "testmail@uus.com": "Test Employee 1"}
# print(employee_dict["testmail@hs.com"])

# dict = chainable and ordered and unordered

# # Tuples
# tuple_example = (123, "Apple", True, 123)
# print(tuple_example)
# print(tuple_example[0])
# # tuple_example[0] = 0
# # print(tuple_example[0])
# # Unchangeable and unordered

# # Python Sets
# set_example = {"test_value", 1, 2, True, True}
# print(set_example)
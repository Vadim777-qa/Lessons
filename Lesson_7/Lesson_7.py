# try, except, finally == with

# print(2/0)

try:
    print(2 / 0)  # working with errors
except ZeroDivisionError:
    print("Please stop dividing by zero")
except ValueError:
    print("Input")
except:
    pass  # pass как заглушка, можно использывать в функциях, циклах и т.д.
finally:
    print("Finally")
print("abc")

# while True:
#     try:
#         result = input("Enter a number: ")
#         int_result = int(result)
#         print(int_result)
#         break
#     except:
#         continue

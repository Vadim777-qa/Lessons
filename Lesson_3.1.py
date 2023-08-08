list_int = ["Hello", 8, "Worlds"]
dict_one = {"Ford": "Car_1",
            "Hyundai": "Car_2",
            "Nissan": "Car_1"}
print(dict_one.values())
tuple_one = (7, "Day", "Night", 8)

unique_symbols = input("Enter your string to count symbols: ")
result = len(set(unique_symbols))
print(f"Number of symbols: {result}")

if len(set(unique_symbols)) > 10:
    print("Your number has more than 10 unique symbols: " + "True")
else:
    print("Your number has less than 10 unique symbols: " + "False")
get_range = range(1, 101)

for number in get_range:
    if (number % 5 == 0 and number % 7 == 0):
        print("ChickenMonkey")
    elif (number % 5 == 0 and number % 7 != 0):
        print("Chicken")
    elif (number % 5 != 0 and number % 7 == 0):
        print("Monkey")
    else:
        print(number)



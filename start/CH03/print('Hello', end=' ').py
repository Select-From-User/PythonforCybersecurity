good_day = input("is today a good day? (y/n): ")
number = 1
while number <= 10:
    if good_day == "y":
        number = number + 1
        print("Yes it is")

print("welcome to day 3")

# if_else

height = int(input("What is your height? "))
if height < 6:
    print(f"Here is your height {height}")
else:
    print("Invalid height ")

number_to_check = int(input("What is your number you want to check ?"))

if number_to_check % 2 == 0:
    print("This is an even number ")
else:
    print("This is an odd number ")

# Nested if_else
height = int(input("What is your height in cm ?"))
if height >= 120:
    print("You can ride boat")
    age = int(input("Write your age"))
    if age >=18:
        print("Okay you are eligible for a boat ride")
    else:
        print("Not eligible ")
else:
    print("Sorry hopefully you will be able to ride boat later")
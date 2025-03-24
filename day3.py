# print("welcome to day 3")
#
# # if_else
#
# height = int(input("What is your height? "))
# if height < 6:
#     print(f"Here is your height {height}")
# else:
#     print("Invalid height ")
#
# number_to_check = int(input("What is your number you want to check ?"))
#
# if number_to_check % 2 == 0:
#     print("This is an even number ")
# else:
#     print("This is an odd number ")
#
# # Nested if_else
# height = int(input("What is your height in cm ?"))
# if height >= 120:
#     print("You can ride boat")
#     age = int(input("Write your age"))
#     if age >=18:
#         print("Okay you are eligible for a boat ride")
#     else:
#         print("Not eligible ")
# else:
#     print("Sorry hopefully you will be able to ride boat later")

# print(r'''
#  _               _           _       _
# | |             | |         (_)     | |
# | |__   __ _  __| |_ __ ___  _ _ __ | |_ ___  _ __
# | '_ \ / _` |/ _` | '_ ` _ \| | '_ \| __/ _ \| '_ \
# | |_) | (_| | (_| | | | | | | | | | | || (_) | | | |
# |_.__/ \__,_|\__,_|_| |_| |_|_|_| |_|\__\___/|_| |_|
# ''')
#
# print('\'You "are" Eshan.')

print("Welcome to the Rollar coaster")
height = int(input("Drop your height :"))

if height >= 120:
    print("You can ride rollar coaster ")
    age = int(input("What is your age ?"))
    if age >= 18:
        print("You can ride it ")
    else:
        print("Sorry better luck next time")
else:
    print("You have to wait")

wants_photo = input("Do you want to take a photo? Press Y for 'YES' and N for 'NO'")
if wants_photo == "Y":
    bill += 3

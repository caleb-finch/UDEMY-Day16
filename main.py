from menu import *
from coffee_maker import *
from money_machine import *

latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
cappuccino = MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)
espresso = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)

print(latte.ingredients)


# off = False
# print("Welcome to BuckStars!")

# while not off:
#     print("====================\nHere is a list of commands you can do\nOff - Turns off the coffee machine\nReport - Shows current machines resources\nResources - Add resources to the machine\nLatte\\Espresso\\Cappuccino\n=======================================")
#     user_choice = ""
#     while user_choice not in ["report", "off", "resources", "latte", "espresso", "cappuccino"]:
#         user_choice = input("What would you like to do? ").lower()
#         if user_choice not in ["report", "off", "resources", "latte", "espresso", "cappuccino"]:
#             print("Invalid choice. Please try again.")
#     #user_choice = "Report"
#     if user_choice == "report":
#         output_report(resources)
#     elif user_choice == "off":
#         off = True
#         print("Shutting down...")
#         break
#     elif user_choice == "resources":
#         resources = add_resources(resources)
#     else:
#         for list in MENU:
#             if user_choice == list:
#                 make_coffee(resources, MENU[list], list)
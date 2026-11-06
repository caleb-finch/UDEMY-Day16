from menu import *
from coffee_maker import *
from money_machine import *

# latte = MenuItem(name="latte", cost=2.5, water=200, milk=150, coffee=24)
# cappuccino = MenuItem(name="cappuccino", cost=3, water=250, milk=50, coffee=24)
# espresso = MenuItem(name="espresso", cost=1.5, water=50, milk=0, coffee=18)

coffee_menu = Menu()
buckstarsCPU = CoffeeMaker()
buckstarsT1500 = MoneyMachine()
user_choice = "latte"
print(coffee_menu.find_drink(user_choice))

# coffee_menu = Menu()
# #print(coffee_menu.get_items())

#


# buckstarsCPU = CoffeeMaker()
# print(buckstarsCPU.is_resource_sufficient(coffee_menu.find_drink("latte")))

# buckstarsT1500 = MoneyMachine()

# print(buckstarsT1500.report())
# print(buckstarsT1500.make_payment(coffee_menu.find_drink("latte").cost))

####################################################################################
coffee_menu = Menu()
buckstarsCPU = CoffeeMaker()
buckstarsT1500 = MoneyMachine()
off = False
while not off:
    print("Welcome to BuckStars! Please pay attention as our menu has changed.")
    print("====================\nHere is a list of commands you can do\nOff - Turns off the coffee machine\nReport - Shows current machines resources\nResources - Add resources to the machine\nLatte\\Espresso\\Cappuccino\n=======================================")
    # user_choice = "latte"
    user_choice = input("What would you like to do? ").lower()
    if user_choice == "report":
        print(buckstarsT1500.report())
    if user_choice == "off":
        print("Shutting down...")
        off = True
    if user_choice == "resources":
        print(buckstarsCPU.report())
    else:
        for coffee in coffee_menu.menu:
            if user_choice == coffee.name:
                coffee_order = coffee_menu.find_drink(user_choice)
                if buckstarsCPU.is_resource_sufficient(coffee_order):
                    if buckstarsT1500.make_payment(coffee_order.cost):
                        buckstarsCPU.make_coffee(coffee_order)

                
        

########################################################################################
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
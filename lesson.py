# from turtle import *

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")

# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.forward(100)
# my_screen.exitonclick()


from prettytable import PrettyTable

x = PrettyTable()

x.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
x.add_column("Type", ["Electric", "Water", "Fire"])


x.align = "r"
print(x)
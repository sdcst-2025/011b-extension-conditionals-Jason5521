from rich import print
from os import system
system("clear||cls")

print("[red on white]You decide to break into the lighthouse.")
print("")
print("Inspecting the door for weaknesses, you find nothing.")
print("")
print("However, the wall next to the door has a small hole in it.")
print("")
print("You reach into the hole.")
print("")
print("Your hand pushes against something, and a beep can be heard.")
print("")
print("The front door unlocks and opens, from one button in the wall.")
print("")
print("You cover up the hole with some dirt and head inside.")
print("")
print("Within the lighthouse lies a radio, a device of unknown origin, and the stairs to the top.")
print("")
choice = input("To try and use the radio, enter a 9. to go up the stairs, enter a 13.")
if choice == "9":
    import page9
elif choice == "13":
    import page13
else:
    import page10

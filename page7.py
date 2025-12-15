from rich import print
from os import system
system("clear||cls")

print("As you walk down the path to the gate, you notice a car that has crashed into a tree.")
print("")
print("A quick inspection reveals claw marks on the doors, and broken glass. Lots of broken glass, as if every window in the car shattered.")
print("")
print("Finding nothing of value, you leave the crashed car behind.")
print("")
print("Eventually, you reach the gate.")
print("")
print("The gate is locked tight, and something reminiscient of barbed wire is spread all over the top.")
print("")
print("On the wall next to the gate, there is a terminal.")
print("")
print("Perhaps this terminal can be used to unlock the gate.")
print("")
print("Or, you can try and jump over the gate, barbed wire and all.")
print("")
choice = input("To try your hand at the terminal, enter an 11. to attempt to jump over the gate, enter a 16.")

if choice == "11":
    import page11
elif choice == "16":
    import page16
else:
    import page10
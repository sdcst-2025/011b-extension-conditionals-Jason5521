from rich import print
from os import system
system("clear||cls")

print("You charge down the path to the lighthouse.")
print("")
print("The creature cannot catch up with you.")
print("")
print("You made it to the lighthouse, but the light is off.")
print("")
print("At the entrance, you spot a sign that reads,")
print("""[white on red]'
      MESSAGE FROM THE CRYPTID CONTAINMENT CENTER
      WARNING

     UNIDENTIFIED QUADRIPED SPECIES DETECTED IN FOREST VICINITY 
      DO NOT APPROACH
      EXIT THE FOREST IMMEDIATELY
      EXITS WILL BE SEALED AFTER 10:00 PM'""")
print("")
print("[black underline]This can't be happening[/black underline], you think to yourself.")
print("")
print("You don't know the exact time, sure, but it cannot be that late already.")
print("")
print("further down the path is where the gate should be.")
print("")
choice = input("to go further down, enter a 7. To try and break into the lighthouse, enter an 8. To turn around, enter a 3.")
if choice == "7":
    import page7
elif choice == "8":
    import page8
elif choice == "3":
    import page3
else:
    import page10
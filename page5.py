from rich import print
from os import system
system("clear||cls")

print("Treading deeper into the forest proves to be harder than expected.")
print("")
print("There are holes in the ground big enough to trip and fall in, scattered across the observable ground.")
print("")
print("You wonder if these holes were man-made.")
print("")
print("Out of nowhere, a voice stops you on the path.")
print("")
print("[bold red]<Hey, hey! Stop! Stop right there! You can't go through there, it's too dangerous!>")
print("")
print("It sounds like a woman's voice, but you can't tell where it came from.")
print("")
print("[bold red]<Go left, You'll be safe on the planks!>")
print("")
print("A choice presents itself: you can[bold red underline]Trust the voice and go left[/bold red underline], or you can [bold green underline]run in the opposite direction[/bold green underline].")
print("")
choice = input("To go left, enter a 4. to go the opposite way, enter a 12.")
if choice == "4":
    import page4
elif choice == "12":
    import page12
else:
    import page10
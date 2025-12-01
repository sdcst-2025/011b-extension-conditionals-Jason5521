from os import system
system("clear||cls")

print("Page 1: The welcome page")
print("")
print("This page makes use of the os module's system command to clear the screen")
print("")
print("""To go to the next page, enter a 5.
To stay here, enter anything else.
      """)
choice = input("Where do you want to go next? hint: enter a 5")
if choice == "5":
    import page5
else:
    import page10
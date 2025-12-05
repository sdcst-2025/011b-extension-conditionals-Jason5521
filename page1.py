from os import system
system("clear||cls")

print("You find yourself lost in a cold, dark forest.")
print("")
print("Some insect-like creature has made your lunchbox it's final resting place.")
print("")
print("""On top of that, you hear something approaching. the footsteps rattle the earth beneath your feet. You must run.
      before you are two paths: one path that leads to a lighthouse, another path that leads deeper into the forest.
      """)
choice = input("to pick the forest path, enter a 5. to pick the lighthouse path, enter a 2.")
if choice == "5":
    import page5
elif choice == "2":
    import page2
else:
    import page10
import lib_editor

print("Evergreen state editor (CLI)")
print("----------------------------\n")

print("[1] - Create a new state.")
print("[2] - Edit and existing state.")
print("[0] - Quit state editor.\n")

choice = input("Choice: ").strip()
if choice == "1":
    lib_editor.create_new()

elif choice == "2":
    pass

elif choice == "0":
    pass

else:
    pass
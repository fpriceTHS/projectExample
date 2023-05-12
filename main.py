#Menu Subroutines

"Example Code for A level project"
def display_menu():
    "Function for displaying Menu"
    print("option 1")
    print("option 2")
    print("option 3")

def get_menu_option():
    "Getting menu option"
    return int(input("Enter option : "))

display_menu()
option = get_menu_option()

print(option)

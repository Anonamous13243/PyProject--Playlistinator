# The name check protects the program whilst debugging
if __name__ == "__main__":
    '''Dictionary import for user interaction''' 
    from Dictionary import main
    index = 1
    for interface in main.keys():
        print(f"{index} - {interface}")
        index += 1
    key = int(input("Enter the genre name by number: \n"))
    key -= 1
    keys = list(main.keys())
    key = keys[key] 
    subgenre = main.get(key)
    for sub, serial in subgenre.items():
        print(sub, serial)
    '''End of first for check'''
    user_input = main.keys()
    serial = int(serial)
    '''Secondary check for the subgenre, after this it will continously loop for more inputs'''
    for serial in user_input:
        print(input("\nNow, type the corresponding serial. \n\
The serials (which name subclasses) should be printed above this guide. \n\
------------------------------------\n"))
        break
    print(f"You have selected {serial}")
# If I were to have made a filesystem interactor the continous loop would have assigned genre interactions.
# 
# File organisation, and as an extension the genre organiser would have been sorted in a separate file named 'organiser',
# but the code behind it would've taken too long.

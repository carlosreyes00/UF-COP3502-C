from pakudex import Pakudex
from pakuri import Pakuri


def print_menu():
    print("""Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit\n""")


print("Welcome to Pakudex: Tracker Extraordinaire!")
capacity = 0
while capacity == 0:
    try:
        capacity = int(input("Enter max capacity of the Pakudex: "))
        while capacity < 0:
            print("Please enter a valid size.")
            capacity = int(input("Enter max capacity of the Pakudex: "))
    except Exception as e:
        print("Please enter a valid size.")

print(f"The Pakudex can hold {capacity} species of Pakuri.\n")

pakudex_instance = Pakudex(capacity)

print_menu()

user_input = int(input("What would you like to do? "))
while user_input not in range(1, 7):
    print("Unrecognized menu selection!\n")
    print_menu()
    user_input = int(input("What would you like to do? "))

if user_input == 6:
    print("Thanks for using Pakudex! Bye!")

while user_input != 6:
    if user_input == 1:
        if pakudex_instance.get_size() > 0:
            print("Pakuri In Pakudex:")
            for index, species in enumerate(pakudex_instance.get_species_array()):
                print(f"{index + 1}. {species}")
            print()
        else:
            print("No Pakuri in Pakudex yet!")
            print()

    elif user_input == 2:
        species = input("Enter the name of the species to display: ")
        stats = pakudex_instance.get_stats(species)

        if stats is None:
            print("Error: No such Pakuri!")
            print()
        else:
            print("\nSpecies:", species)
            print("Attack:", stats[0])
            print("Defense:", stats[1])
            print("Speed:", stats[2])
            print()

    elif user_input == 3:
        if pakudex_instance.get_size() == capacity:
            print("Error: Pakudex is full!")
        else:
            pakuri_to_add = input("Enter the name of the species to add: ")

            if pakudex_instance.add_pakuri(pakuri_to_add):
                print(f"Pakuri species {pakuri_to_add} successfully added!")
            else:
                print("Error: Pakudex already contains this species!")

        print()

    elif user_input == 4:
        pakuri_to_evolve = input("Enter the name of the species to evolve: ")

        if pakudex_instance.evolve_species(pakuri_to_evolve):
            print(f"{pakuri_to_evolve} has evolved!")
        else:
            print("Error: No such Pakuri!")

        print()

    elif user_input == 5:
        pakudex_instance.sort_pakuri()
        print("Pakuri have been sorted!\n")

    elif user_input == 6:
        print("Thanks for using Pakudex! Bye!")

    print_menu()
    user_input = 0
    while user_input == 0:
        try:
            user_input = int(input("What would you like to do? "))
            while user_input not in range(1,7):
                print("Unrecognized menu selection!\n")
                print_menu()
                user_input = int(input("What would you like to do? "))
        except Exception as e:
            print("Unrecognized menu selection!\n")
            print_menu()
            user_input = int(input("What would you like to do? "))

    if user_input == 6:
        print("Thanks for using Pakudex! Bye!")
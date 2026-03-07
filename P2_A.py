import console_gfx


def print_menu():
    print('''\nRLE Menu
--------
0. Exit
1. Load File
2. Load Test Image
3. Read RLE String
4. Read RLE Hex String
5. Read Data Hex String
6. Display Image
7. Display RLE String
8. Display Hex RLE Data
9. Display Hex Flat Data\n''')

def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)

    while True:
        print_menu()
        user_option = int(input("Select a Menu Option:"))

        if user_option == 0:
            break
        elif user_option == 1:
            file_to_load = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(file_to_load)
        elif user_option == 2:
            image_data = console_gfx.test_image
            print("Test image data loaded.")
        elif user_option == 6:
            print("Displaying image...")
            console_gfx.display_image(image_data)

if __name__ == "__main__":
    main()















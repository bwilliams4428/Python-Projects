from Functions import *

filename = "coordinates.csv"
colist = []
display_menu()

user_choice = input("You chose option: ")

if user_choice == '1':
    process_file(filename, colist)
    generate_map(colist)

elif user_choice == '2':
    file_path = str(input("Please input full file path:"))
    print(file_path)
    process_file(file_path, colist)
    generate_map(colist)
else:
    print("Exiting...Good Bye!")

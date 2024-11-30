# Use the data in the text_file_editor.py to direct the program on which row it should start to read
# Projectedly, use indices and list to guide the user what information is entered 
# If the user input match a value, use its index to print the row it belong to



def editor_file_check():
    # Links the output of text editor with reader
    # This block should be constant, unless the program's settings are to be modified
    while True:
        try:
            with open("text_file_editor.txt", "r") as file:
                filter_list = []
                for line in file:
                # Removes the spaces between lines
                    line = line.strip()
                    filter_list.append(line)
            
            # Check whether the file has enough lines to satisfy the program
            if not filter_list or len(filter_list) < 5:
                print("The file is empty or has invalid structure. Please make sure the file has valid data and structure first")
                print("Sol: Use text_file_editor.py first")
                quit()
            else:
                # Locates the name and inputs within the file
                file_path = filter_list[2]
                name_list = filter_list[4:]
                if file_path != None and name_list != None:
                    return file_path, name_list
                else:
                    print("File is unable to be processed. Use text_file_editor first")

        except FileNotFoundError:
            print("Please use the text_file_editor first or change the text_file_editor.txt according to the path of your desired file")

# Reads through the lines of the txt file using the user_input and indices
def info_reader():
    file_path, name_list = editor_file_check()
    print(f"You're currently searching in the the {file_path}.txt file")
    print(f"You may use this list as a guide in locating information of users:\n{name_list}")
    while True:
        user_input = input("Enter the full name of the user to see their profile (Press 'q' to quit): ")
        try:
            if user_input in name_list:
                for index, value in enumerate(name_list):
                    if user_input == value:
                        with open(f'{file_path}.txt', 'r') as file:
                            information = file.readlines()
                            return information[index].strip()
            elif user_input.lower() == 'q':
                warning = input("Do you really want to exit? (Press any keys to proceed; 'n' to cancel): ")
                if warning != 'n':
                    print("You have exited the program. Have a nice day!")
                    quit()
            else:
                print(f"Information in the {file_path} not found. Please try again")

        except FileNotFoundError:
            print("Information specified not found. Please check the file path and its content first")

def frontend_prompt():
    print(info_reader())

    while True:
        user_option = input("Do you want to see more profiles? (press 'y' to proceed; 'n' to exit): ").lower()
        if user_option == "y":
            info_reader()
        elif user_option == "n":
            break
        else:
            print("Please respond with only what's specified")
    
    print("Thank you for using the program")

frontend_prompt()
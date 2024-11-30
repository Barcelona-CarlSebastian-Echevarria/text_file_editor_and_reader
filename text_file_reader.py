# Use the data in the text_file_editor.py to direct the program on which row it should start to read
# Projectedly, use indices and list to guide the user what information is entered 
# If the user input match a value, use its index to print the row it belong to


# Links the output of text editor with reader
# This block should be constant, unless the program's settings are to be modified
with open("text_file_editor.txt", "r") as file:
    filter_list = []
    for line in file:
      # Removes the spaces between lines
      line = line.strip()
      filter_list.append(line)

# Locates the name and inputs within the file
file_path = filter_list[2]
name_list = filter_list[4:]

# Reads through the lines of the txt file using the user_input and indices
while True:
    print(f"You're currently searching in the the {file_path}.txt file")
    print(f"You may use this list as a guide in locating information of users:\n{name_list}")
    user_input = input("Enter the full name of the user to see their profile (You can use the list above as guide): ")
    if user_input in name_list:
        for index, value in enumerate(name_list):
            if user_input == value:
                with open(f'{file_path}.txt', 'r') as file:
                    information = file.readlines()
                    print(information[index].strip())
    else:
        print(f"Information in the {file_path} not found. Please try again")

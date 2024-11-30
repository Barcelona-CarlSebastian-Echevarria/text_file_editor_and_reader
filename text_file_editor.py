# Create a dedicated txt file for the user; name of file is of user's desire
# Upon file creation, profile the user with essential questions; the output shall be written in the file
# Give the user the privilege to input more information; otherwise, give the user option to exit
# Format the inputs in the txt file-- make it visually appealing as much as possible
# Draft: Ask the user whether they want to create another file for another profiling
# Draft: Store each file name in a list for navigation and latter edits

profiles_list = []
file_list = []
# Creates a bridging file to connect the editor and the reader
# The file created here is not permanent
def data_path(file_list, profiles_list):
    with open("text_file_editor.txt", "w") as file:
        file.write("Note: The following data is uploaded via text_file_editor.py. You can access it via the text_file_reader.py")
        for name in file_list:
            file_name = name
        file.write(f"\nFile name:\n{file_name}\nProfiles:")
        for profile in profiles_list:
            file.write(f"\n{profile}")

# Obtains the user full name
def user_full_name():
    while True:
        special_cases = ["-", "'", "."]
        user_name = input("Enter your full name: ")
        user_name = user_name.split()
        name = (''.join(user_name))
        if len(name) >= 2:
            if any(elements in special_cases for elements in name) or name.isalpha():
                    name = (' '.join(user_name))
                    # Makes the first letters of the words capitalized
                    name = name.title()
                    profiles_list.append(name)
                    return name
            else:
                print(f"Name contains invalid characters. Only letters, digits, and {special_cases} are allowed.")
        else:
            print("Enter a valid name")

# Obtains the user age
def user_age():
    while True:
        try:
            user_age = int(input("Enter your age (input must be realistic): "))
            # 122 is the limit, for it's the oldest age recorded for a human
            if 0 < user_age <= 122:
                return user_age
            else:
                print("Please enter a valid age")
        except ValueError:
            print("Enter a numerical input only")

# Obtains user address
def user_full_address():
    special_cases = ["-", "'", ".", ",", "/"]
    while True:
        user_address = input("Enter your full address (Max of 60): ")
        user_address = user_address.split()
        valid_address = (''.join(user_address))
        if 11 <= len(valid_address) <= 60:
            if any(elements in special_cases for elements in valid_address) or valid_address.isalnum():
                    valid_address = (' '.join(user_address))
                    user_address = valid_address.title()
                    return user_address
            else:
                print(f"Address contains invalid characters. Only letters, digits, and {special_cases} are allowed.")
        else:
            print("Enter a valid address (must be more than 10 characters long)")

# Obtains the user contact number
def user_contact_number():
    while True:
        try:
            user_number = int(input("Enter your contact number (input must be 11 characters only): +63|"))
            user_number = str(user_number)
            if user_number.isdigit() and len(user_number) == 10:
                  return f"+63{user_number}"
            else:
                  print("Please enter a valid contact number")
        except ValueError:
            print("Enter a numerical input only")

# Obtains the user religion
def user_official_religion():
    religions = ["Christianity", "Islam", "Hinduism", "Buddhism", "Judaism", "Sikhism", "Not in the list"]
    print("Choose which faith you're affiliated with from the following list:")
    for index, value in enumerate(religions):
        print(f"{index + 1}. {value}")

    while True:
        user_religion = int(input("Press 1-7 to choose your religion: "))
        if user_religion not in range(1, 8):
            print("Please enter a response from the range specified")
        else:
            for index, value in enumerate(religions):
                if user_religion == index + 1:
                 return f"{value}"
                
# Obtains the user blood type
def user_blood_type():
    blood_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    print(f"You may choose your type from the following list:")
    for index, value in enumerate(blood_types):
     print(f"{index + 1}. {value}")

    while True:
        user_type = int(input("From left to right, press 1-8 to choose your type: "))
        if user_type not in range(1, 9):
            print("Please enter a response from the range specified")
        else:
            for index, value in enumerate(blood_types):
                if user_type == index + 1:
                 return f"{value}"

# Formats the information obtained
# Will determine the format of the information within the txt file
def text_format():
    name = user_full_name()
    age = user_age()
    address = user_full_address()
    contact_number = user_contact_number()
    religion = user_official_religion()
    blood_type = user_blood_type()
    return f"Name: {name} | Age: {age} | Address: {address} | Contact Number: {contact_number} | Religion: {religion} | Blood Type: {blood_type}"

# Converts the inputted name into snake_case and creates a txt file with the name 
def create_file_name():
    while True:
        print("The program will automatically convert the name into snake case")
        user_input = input("What do you want to name your txt file?: ")
        if user_input.isdigit():
            print("Please enter a valid name (Pure numerical name is not allowed)")
        else:
            index_list = []
            # Converts the name in a camel_case format if there's no occurrence of a number within the name
            user_input = user_input.lower()
            user_input = user_input.split()
            user_input = ('_'.join(user_input))
            # The idea of the if-block was sourced from geeksforgeeks.org, stackoverflow.com and was tailored accordingly for the program
            # Checks for the occurrence of a number within the name and stores its index
            if any(num.isdigit() for num in user_input):
                for index, inputs in enumerate(user_input):
                    if inputs.isdigit():
                        num_position = index
                        index_list.append(num_position)
                # Adds an underscore in the index of the first number within the name using the smallest index from index_list
                index_of_number = min(index_list)
                for indices in range(len(user_input)):
                    if indices == index_of_number:
                        valid_name = user_input[:index_of_number] + "_" + user_input[index_of_number:]
                        return valid_name
            else:
                valid_name = user_input
                return valid_name

# Handles all the program's functionalities
def main():
    file_name = create_file_name()
    # Temporarily stores the name of the txt file
    file_list.append(file_name)
    with open(f"{file_name}.txt", "a") as file:
        file.write(text_format())

        # Asks the user if it wants to add additional information
        while True:
            user_option = input("Do you want to add more information? (press 'y' to proceed; 'n' to exit): ")
            if user_option == 'y':
                file.write(f"\n{text_format()}")
            elif user_option == 'n':
                # Used to define the name of the list when uploaded to the txt file
                data_path(file_list, profiles_list)
                print("Data has been successfully uploaded. Please proceed to text_file_reader.py")
                break
            else:
                print("Please respond with only what's specified")

    
main()
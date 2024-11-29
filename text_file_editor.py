# Create a dedicated txt file for the user; name of file is of user's desire
# Upon file creation, profile the user with essential questions; the output shall be written in the file
# Give the user the privilege to input more information; otherwise, give the user option to exit
# Format the inputs in the txt file-- make it visually appealing as much as possible
# Draft: Ask the user whether they want to create another file for another profiling
# Draft: Store each file name in a list for navigation and latter edits

def question_one():
    while True:
        special_cases = ["-", "'", "."]
        user_name = input("Enter your full name: ")
        user_name = user_name.split()
        name = (''.join(user_name))
        if name.isalpha() and len(name) >= 2:
            break
        # Checks if there's an occurrence of special characters within the name
        elif any(elements in special_cases for elements in name): 
            break
        else:
            print("Enter a valid name")

    name = (' '.join(user_name))
    # Makes the first letters of the words capitalized
    name = name.title()
    return name

def create_file_name():
    while True:
        print("The program will automatically convert the name into camel_case")
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

def main():
    file_name = create_file_name()
    # Creates a txt file and appends the input from question functions
    with open(f"{file_name}.txt", "a") as file_name:
        # Not yet finalized, for draft only
        file_name.write(question_one())
        
        # Asks the user if it wants to add additional information
        while True:
            user_option = input("Do you want to add more information? (press 'y' to proceed; 'n' to exit): ")
            if user_option == 'y':
                file_name.write(question_one())
            elif user_option == 'n':
                quit()
            else:
                print("Please respond with only what's specified")

main()
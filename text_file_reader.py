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

file_path = filter_list[2]
name_list = filter_list[4:]
print(file_path)
# Not yet working
print(name_list)

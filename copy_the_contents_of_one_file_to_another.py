Develop a script to copy the contents of one file to another.

with open("test.txt", "r") as source_file:
    content = source_file.read()

with open("copy_test.txt", "w") as destination_file:
    destination_file.write(content)

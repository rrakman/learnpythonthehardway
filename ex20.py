from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)#pydoc file.seek,anyways it means with param 0 go to top of the file

def print_a_line(line_count,f):
    print(line_count,f.readline())#pydoc file.readline

current_file = open(input_file)

print("first let s print the whole file: \n")
print_all(current_file)
print("now let s rewind, kind of like a tape.")
rewind(current_file)
print("lets print three lines :")
current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

from sys import argv
script, filename = argv

print(f"We re going to erase {filename}. if you don t wanna do this pressq CTR+'C'")
input("?")
print("Opening the file....")

target = open(filename,'r+')

print("truncating the file. good bye!")
target.truncate()
print("now, im going to ask you for two lines.")
line1 = input("line 1 : ")
line2 = input("line 2 : ")
print("i m going to write these to the file.")

target.write(f"{line1}\n{line2}\n")

print("and finally, we close it.")
target.close()

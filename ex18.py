#def print_two(*args):
#    arg1, arg2 = args
#    print(f"arg1: {arg1}, arg2: {arg2}")

#no need for *args
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
#one arg
def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("i got nothin'.")

#print_two("reda","rakman")
print_two_again("reda","rakman")
print_one("hamouda")
print_none()

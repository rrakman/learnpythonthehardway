def add(a, b):
    print(f"Addding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("let s do some math with just funtions !")

age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age : {age}, Height : {height}, Weight : {weight} iq : {iq}")

#bonus puzzle
a=1
b=2
c=3
d=4
#1+2-3*4/2=-3
print("here is a puzzle.")


what = add(a , subtract(b,multiply(c, divide(d,2))))
print("that becomes :", what,"can you do it by hand ?")
# i learnt how to play with function with this exercise.

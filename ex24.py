print("let s practice everything.")
print('You\'d need to know \'bout escapes with \\ that do : ')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely work
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhre there is none.
"""
print("-----------------")
print(poem)
print("-----------------")

five = 10 - 2 + 3 - 6
print(f"this should be five : {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans,jars,crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)
#another way to format a string
print("With a starting point of : {}".format(start_point))
#this is like the f"" string
print(f"we'd have {beans} beans,{jars} jars,and {crates} crates.")

start_point = start_point / 10

print("we'd also do this way : ")
formula = secret_formula(start_point)
#this is an easy way to aplly a list to a format string
print("we'd have {} beans, {} jars, and {} crates".format(*formula))

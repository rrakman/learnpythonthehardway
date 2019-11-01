from sys import argv
script, user_name = argv
first, second = ARGV
print(f"{first}{second}")
prompt = '> '

print(f"Hi {user_name},I'm the {script} script.")
print("I d like to ask you a few questions.")
print(f"Do you like me {user_name} ?")

like = input(prompt)


print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computers do you have ?")
computer = input(prompt)

print(f"""
Alright, so you said {like} about liking me.
You live in {lives}. not sute where that is.
And you have a {computer} computer. Nice
""")

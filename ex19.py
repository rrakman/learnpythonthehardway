def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses !")
    print(f"you have {boxes_of_crackers} boxes of crackers !")
    print("man thats enough for party")
    print("get a blanket\n")


print("we can just give the funtion numbers directly: ")
cheese_and_crackers(20, 50)

print("or we can use variables from ou script : ")
amount_of_cheese = 10
amount_of_crackers = 20

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside too : ")
cheese_and_crackers(10+20,5+12)

print("and we can combine the two variables and math :")
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers+1000)

#so in this exo i learnt the syntax of function and how to integrate variables and maths inside.
#this is study drill , i m creating a funtion that takes emails from input then add them to a text file
def collect_emails_in_text_file(email):
    print(f"{email}")
    out_file = open("email.txt",'a')
    out_file.write(email + '\n')
    out_file.close()

email=input("tape your email here :")
collect_emails_in_text_file(email)

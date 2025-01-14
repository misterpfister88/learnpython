menu = "Pizza, Doner, Burger"
price = 10

print("Hello, welcome to the restaurant!")
name = input("What is your name? ")


    
   
choice = input("Hello, here is the Menu, what do you want to eat?\n"+menu+ "\n")
quantity= input("How many "+ str(choice) + " do you want? ")
total= int(quantity) * price
print("Your total is "+ str(total))
print("Thanks for the order, your " + str(quantity) +" " + str(choice) + " will be ready soon.")
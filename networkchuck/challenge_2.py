menu = "Pizza, Doner, Burger"
price = 10
choice = input("Hello, here is the Menu, what do you want to eat?\n"+menu+ "\n")
quantity= input("How many "+ choice+ " do you want? ")
total= int(quantity) * price
print("Your total is "+ str(total))
print("Thanks for the order, your " + quantity +" " + choice + " will be ready soon.")
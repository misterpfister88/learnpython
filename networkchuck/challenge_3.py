order = input("What do you want to order? ")

if order == "Pizza":
    print("Pizza costs 10")
elif order == "Doner":
    print("Doner costs 5")
    extras= input("Do you want extras? ")
    if extras == "Yes":
        print("Extras cost 2")
    else:
        print("No extras")

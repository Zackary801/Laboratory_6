age = int(input("what is your age? "))
membership = input("are you a member? ")
if age <= 17 and age >= 1 and membership == "yes":
    print("Your payment will be 450.00")
elif age <= 17 and age >= 1 and membership == "no":
    print("Your payment will be 650.00") 
elif age >= 17 and age < 65 and membership == "yes": 
    print("Your payment will be 550.00")
elif age >= 17 and age < 65 and membership == "no": 
    print("Your payment will be 750.00")
elif age > 65 and membership == "yes":
    print("Your payment will be 400 ")
elif age > 65 and membership == "no":
    print("Your payment will be 600.00 ")
else:
    print("There seems to be a problem with your age or mebership please try again later")

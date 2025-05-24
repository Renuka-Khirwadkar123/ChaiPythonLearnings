size=input(f"Enter your preference: Small/Medium/Large: ")
extrashot=input(f"Extra shot needed Yes/No: ")

if extrashot=="Yes":
    activity=f"Ordered {size} with extrashot"
else:
    activity=f"coming up {size} mocha"


print(activity)
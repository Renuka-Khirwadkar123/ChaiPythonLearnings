animal="Lion"
age=10

if animal!="Dog" and animal!="Cat":
      print(f"No data available for {animal}")
      exit()

if animal=="Dog" and age<2:
      print("AI recommends puppy food")
elif animal=="Cat"and age>5:
      print("AI recommends senior cat food")
else:
      print(f"No data present for {animal} with {age}")

distance=-1
if distance<=0:
    print("Enter valid distance")
    exit()
       
if distance<3:
    print("You should prefer walk")
elif distance<=15:
    print("You should use bike for commute")
elif distance>15:
    print("You should take a car")
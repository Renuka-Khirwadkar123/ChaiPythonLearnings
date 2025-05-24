password="123456"

if len(password)<6:
    print("Password is weak")
elif len(password)<=10:
    print("Medium")
elif len(password)>10:
    print("Strong")

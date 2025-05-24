def name(**kwargs):
    for k,v in kwargs.items():
       return f"{k},{v}"

print(name(Ironman="Iron",Thor="Hammer"))
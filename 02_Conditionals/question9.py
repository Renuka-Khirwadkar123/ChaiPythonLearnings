year=2025

if (year%4==0 and year%100!=0) or year%400==0:
   print(f"{year} is leap year")
else:
    print(f"{year} is non leap year")

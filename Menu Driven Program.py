# Menu Driven Program

user_input = input(''' 

1. Convert cm to inches
2. Convert Km to miles
3. Convert usd to inr
4. Exit
''')

if user_input == "1":
  cm = float(input("Enter value in CM: "))
  inches = cm * 0.394
  print("The value in Inches is: ",inches)
elif user_input == "2":
  km = float(input("Enter value in Km: "))
  mile = km * 0.621
  print("The value in Miles is: ",mile)
elif user_input == "3":
  usd = float(input("Enter value in USD: "))
  inr = usd * 76.63
  print("The value in INR is: ",inr)
else:
  print("Exit")



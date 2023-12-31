# Determine Weather Type

Temp = int(input("Enter the Temperature: "))
Humidity = int(input("Enter the Humidity: "))

if Temp>= 30 and Humidity >= 90:
  print("Hot and Humid")
elif Temp >= 30 and Humidity < 90:
  print("Hot")
elif Temp <30 and Humidity >= 90:
  print("Cold and Humid")
else:
  print("Cold") 
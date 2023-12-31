# Calculate Profit or Loss
"""
Formula:

Profit: SP - CP
Loss: CP - SP
"""

cp = float(input("Enter the Cost Price: "))
sp = float(input("Enter the Selling Price: "))

if cp > sp:
  amount = cp - sp
  print("Loss: ",amount)
else:
  amount = sp - cp
  print("Profit: ",amount)


Input: [(1, 'apple'), (2, 'banana'), (3, 'orange')]
Output:  apple banana orange

results = [(1, 'apple'), (2, 'banana'), (3, 'orange')]

# Initialization
text = " "

# Loop through results
for result in results:
    text += result[1] + " "

# Printing the result
print(text)

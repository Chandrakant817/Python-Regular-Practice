"""input: simple strings are simple
output: s,e,4
"""
x = input("Enter a string: ")

counts = {}

for i in x:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
print(counts)

# Find the maximum occurrence count
max_count = max(counts.values())  
print(max_count)

max_chars = []
for key, value in counts.items():
    if value == max_count:
        max_chars.append(key)

# Displaying the result
result = ",".join(max_chars) + "," + str(max_count)
print(f"The character '{','.join(max_chars)}' occurred {max_count} time the most.")
print(result)

---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------

input_string = input("Enter a string: ")

# Removing spaces and converting the string to lowercase for consistent counting
input_string = input_string.replace(" ", "").lower()

# Counting occurrences of each character
count = {}
for char in input_string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

# Finding the maximum occurrence countff
max_occurrence = 0
for value in count.values():
    if value > max_occurrence:
        max_occurrence = value

# Finding characters with maximum occurrence
max_chars = []
for char, occurrence in count.items():
    if occurrence == max_occurrence:
        max_chars.append(char)

# Displaying the result
result = ",".join(max_chars) + "," + str(max_occurrence)
print(f"The character(s) '{','.join(max_chars)}' occurred {max_occurrence} time(s) the most.")
print(result)

# Example: Division by zero error handling
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print("Result:", result)  # This line will not be executed due to the exception
except ZeroDivisionError as e:
    print("Error:", e)
    print("Cannot divide by zero. Please provide a non-zero denominator.")

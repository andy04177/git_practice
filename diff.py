# Function to calculate the difference between two numbers
def subtract_numbers(num1, num2):
    result = num1 - num2
    return result

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the subtract_numbers function and display the result
difference_result = subtract_numbers(num1, num2)
print(f"The difference between {num1} and {num2} is {difference_result}")

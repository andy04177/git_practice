# Function to add two numbers
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the add_numbers function and display the result
sum_result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {sum_result}")

print("Function created")
# Function to multiply two numbers
def multiply_numbers(num1, num2):
    result = num1 * num2
    return result

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the multiply_numbers function and display the result
product_result = multiply_numbers(num1, num2)
print(f"The product of {num1} and {num2} is {product_result}")



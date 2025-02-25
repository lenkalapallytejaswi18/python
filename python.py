python program

print("hello world")

# Program to add two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}")

# A simple calculator to add two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform addition
result = num1 + num2
print(f"The result is: {result}")

# Program to check whether a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# Program to calculate the factorial of a number
num = int(input("Enter a number: "))
factorial = 1

# Loop to calculate factorial
for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")

# Program to check if a number is prime
num = int(input("Enter a number: "))

# A prime number is greater than 1 and divisible only by 1 and itself
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Program to reverse a string
text = input("Enter a string: ")
reversed_text = text[::-1]
print(f"The reversed string is: {reversed_text}")

# Program to count vowels in a string
text = input("Enter a string: ")
vowels = 'aeiou'
count = 0

# Count vowels
for char in text:
    if char.lower() in vowels:
        count += 1

print(f"The number of vowels in the string is: {count}")

# Program to calculate the sum of digits of a number
num = int(input("Enter a number: "))
sum_digits = 0

# Loop to calculate the sum of digits
while num > 0:
    sum_digits += num % 10
    num = num // 10

print(f"The sum of the digits is: {sum_digits}")

# Program to find the maximum of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"The maximum number is {num1}")
else:
    print(f"The maximum number is {num2}")









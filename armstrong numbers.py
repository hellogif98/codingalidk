# Program to find if a number is an Armstrong number

# Take the input from the u ser
number = int(input(" input your number "))

# Calculate the number of the digits
digits = len(str(number))

# Initialize result variable
resultNumber = 0

# Find the sum from a^digit of each digit
temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digits
    temp //= 10

# Display the result
if number == resultNumber:
    print(number,"is an Armstrong Number") 
else:
    print(number,"is not an Armstrong Number")

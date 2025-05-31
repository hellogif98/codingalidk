# To find factors of user input

# Goes from 1 number and checks if i divide the number. If yes, it is a factor 
def print_factors(numbers):
    print("The factors of", number, "are:")
    for i in range (1, number +1):
        if number % i == 0:
            print(i)

# Taking the input from the user
number = int(input(" enter your number to find if it's a factor:"))

# Calling our function
print_factors(number)
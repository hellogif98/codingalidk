# Program to see if the user inputs are equal without using any comparision operator.

def checkIfSame(number1, number2):

# User XOR operator as a^a is always 0
  if ((number1 ^ number2) !=0):
    print("Numbers are not equal")
  else:
    print("Both numbers are equal")

# Taking input
number1 = int(input("Enter First Number to Compare : "))
number2 = int(input("Enter Second Number to Compare : "))

checkIfSame(number1 , number2)
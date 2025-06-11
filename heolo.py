# To find the LCM number of user input
# Enter 2 numbers

numberLargest = int(input("Enter a Large Number : "))
numberSmallest = int(input("Enter a Small Number : "))
 
# Using Eucliden Algorithms
while (numberSmallest):
    numberStore = numberSmallest 
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore
print("LCM is : ", numberLargest)

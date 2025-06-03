# Program to find HCF/GCD 
# Enter 2 numbers
numberLargest = int(input("Enter The Largest Number : "))
numberSmallest = int(input("Enter The Smallest Number :")) 

# Using Eucliden Algorithms
while (numberSmallest):
    numberStore = numberSmallest 
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore
print("HCF is : ", numberLargest)

# Program to find the 0 bits and 1 bits present in a number

# Functions taking our number as input
def numberOfBits(n):
    ones = 0
    zero = 0

    # While number is greater check last but and right shift
    While (n):

    # Use AND operater to check if last bit is 1 or 0
    if(n&1==1):
        ones+=1
    else:
        zero+=1
    # Right shift the number remove the last bit we just checked above
    n>>=1
    print("/n/n0nes =", ones,"/nZer0s", zeros)

    
int(input("Enter your number : "))
numberOfBits(number)

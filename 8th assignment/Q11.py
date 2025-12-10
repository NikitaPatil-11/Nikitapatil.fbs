#WAP to check if a given number is Armstrong number or not. For each task create separate functions.

# Function to count digits
def countDigits(num):
    return len(str(num))

# Function to calculate Armstrong sum
def armstrongSum(num):
    digits = countDigits(num)
    temp = num
    total = 0
    
    while temp > 0:
        d = temp % 10
        total += d ** digits
        temp //= 10
    
    return total

# Function to check if Armstrong
def isArmstrong(num):
    if num == armstrongSum(num):
        return f"{num} is an Armstrong number."
    else:
        return f"{num} is not an Armstrong number."

# Main program
num = int(input("Enter number: "))
print(isArmstrong(num))

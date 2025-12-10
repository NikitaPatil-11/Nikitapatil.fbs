
# WAP to print Fibonacci series up to n terms

#what is fibonacci series
#The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. 
# The sequence begins as 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on, 
# with the general formula being \(F(n)=F(n-1)+F(n-2)\), where \(F(0)=0\) and \(F(1)=1\). 

n = int(input("Enter the number of terms: "))

a, b = 0, 1   # first two terms of Fibonacci series

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci series:", a)
else:
    print("Fibonacci series:", end=' ')
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b   # update values



#Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

#A number is an Armstrong number if the sum of its digits raised to the power of the number of digits equals the number itself.
#\text{If } n = d_1^p + d_2^p + d_3^p + \dots + d_k^p \Rightarrow \text{Armstrong number}
#Where:- n is the original number
#- d_1, d_2, \dots, d_k are the digits
#- p is the number of digits


# Program to check Armstrong number

num = int(input("Enter a number: "))
original = num
power = len(str(num))
sum_of_powers = 0

while num > 0:
    digit = num % 10
    sum_of_powers += digit ** power
    num = num // 10

if sum_of_powers == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is NOT an Armstrong number.")
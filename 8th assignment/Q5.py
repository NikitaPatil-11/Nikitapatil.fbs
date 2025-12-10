#Sum of all prime numbers between 1 to n
def sum_of_primes(n):    # function with parameter
    total = 0
    
    for num in range(2, n + 1):   # primes start from 2
        is_prime = True

        # check if num is prime
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            total += num

    print("Sum of all prime numbers between 1 and", n, "is:", total)

# Main program
num = int(input("Enter value of n: "))
sum_of_primes(num)

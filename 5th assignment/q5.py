# WAP to print all prime numbers between 1 and 100



print("Prime numbers between 1 and 100 are:")

for num in range(2, 101):       # numbers from 2 to 100
    for i in range(2, num):     # check divisibility from 2 to num-1
        if num % i == 0:        # if divisible, not prime
            break
    else:                       # else runs only if no break occurred → prime
        print(num)

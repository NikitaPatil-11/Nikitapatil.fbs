def fibonacci(n):      # function with parameter
    a, b = 1, 1
    print(a, b, end=" ")   # print first two terms

    for i in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

# Main program
num = int(input("Enter number of terms: "))
fibonacci(num)

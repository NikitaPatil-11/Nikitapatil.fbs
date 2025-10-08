#calculate compund interest
P  = float(input('enter Principal amount (P) : '))
T = float(input('enter total time (T) in years : '))
R = float(input('enter rate of interest (R) % :'))

#compound interest formula
# A=final amount 

A = P * (1 + R / 100) ** T

# Compund interest
CI = A - P 

print(f"\nCompound Interest: {CI:.2f}")
#write a programme to cal. simple interest based on principal,rate and time.
def calculate_simple_interest(principal, rate, time):
    # Simple Interest formula: (P × R × T) / 100
    return (principal * rate * time) / 100

# Input from user
print("Simple Interest Calculator")
principal = float(input("Enter Principal amount (P): "))
rate = float(input("Enter Rate of interest (R) in %: "))
time = float(input("Enter Time period (T) in years: "))

# Calculate interest
interest = calculate_simple_interest(principal, rate, time)

# Output result
print(f"\nSimple Interest = ₹{interest:.2f}")
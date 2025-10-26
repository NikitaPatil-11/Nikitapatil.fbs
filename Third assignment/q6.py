## Program to calculate profit or loss

# Input cost price and selling price
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

# Check for profit, loss or no profit/loss
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"\nYou made a Profit of ₹{profit:.2f}")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"\nYou incurred a Loss of ₹{loss:.2f}")
else:
    print("\nNo Profit, No Loss.")

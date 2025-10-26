# Program to calculate total bill for 5 products after adding 18% GST

# Accept price of 5 products
p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
p4 = float(input("Enter price of product 4: "))
p5 = float(input("Enter price of product 5: "))

# Calculate total
total = p1 + p2 + p3 + p4 + p5

# Calculate GST (18%)
gst = total * 0.18

# Final amount after GST
final_bill = total + gst

# Display results
print("\n------ BILL SUMMARY ------")
print(f"Total (without GST): ₹{total:.2f}")
print(f"GST @18%: ₹{gst:.2f}")
print(f"Total Bill (with GST): ₹{final_bill:.2f}")

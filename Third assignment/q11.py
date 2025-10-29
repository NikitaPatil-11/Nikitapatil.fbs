#Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount   b.Senior citizen (above 59) = 50% discount   c. Others need to pay full.

# Initialize lists to store ages and ticket prices
ages = []
tickets = []

# Accept data for 5 people
for i in range(5):
    age = int(input(f"Enter age of person {i+1}: "))
    price = float(input(f"Enter ticket amount for person {i+1}: "))
    ages.append(age)
    tickets.append(price)

# Calculate total amount
total_amount = 0
for i in range(5):
    if ages[i] < 12:
        discount_price = tickets[i] * 0.7  # 30% discount
    elif ages[i] > 59:
        discount_price = tickets[i] * 0.5  # 50% discount
    else:
        discount_price = tickets[i]  # No discount
    total_amount += discount_price

print(f"Total ticket amount for all 5 people: {total_amount}")

# Accept no. of passengers from user and per ticket cost. 
# Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount   b.Senior citizen (above 59) = 50% discount   c.Others need to pay full.
  

num_passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter cost of one ticket: "))

total_amount = 0

for i in range(1, num_passengers + 1):
    age = int(input(f"Enter age of passenger {i}: "))

    if age < 12:
        discount = 0.30  # 30% discount
        fare = ticket_cost * (1 - discount)
    elif age > 59:
        discount = 0.50  # 50% discount
        fare = ticket_cost * (1 - discount)
    else:
        fare = ticket_cost  # no discount

    total_amount += fare
    print(f"Ticket amount for passenger {i}: ₹{fare:.2f}")

print(f"\nTotal amount to be paid for all passengers: ₹{total_amount:.2f}")

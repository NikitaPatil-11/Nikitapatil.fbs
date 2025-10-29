# Program to calculate ele bill
units = float(input("Enter total electricity units consumed: "))

#Calculate bill according to slabs
if units <= 50:
    amount = units * 0.50
elif units <=150:
    amount = (50*0.50) + ((units - 50)*0.75)
elif units <=250:
    amount = (50*0.50) + (100*0.75) + ((units - 150)*1.20)
else:
    amount = (50*0.50) + (100*0.75) + (100*1.20)+ ((units - 250)*1.50)
    
    
    #add 20% surcharge
    
    surcharge = amount * 0.20
    total_bill = amount + surcharge
    
    
    print(f"\nElectricity Bill details")
    print(f"---------------")
    print(f"Units Consumed   : {units}")
    print(f"Base Amount      :{amount:.2f}")
    print(f"Surcharge (20%)) :  {surcharge:.2f}")
    print(f"Total Bill       :{total_bill:.2f}")
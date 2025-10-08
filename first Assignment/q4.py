#WAP to enter P , T, R AND calculate simple interest
Principal = float(input('enter Principal amount (P) : '))
Time = float(input('enter total time (T) in years : '))
Rate = float(input('enter rate of interest (R) % :'))

#Simple interest formula = p*t*r/100

Simple_interest= (Principal*Time*Rate)/100

print('Simple interest =',Simple_interest)
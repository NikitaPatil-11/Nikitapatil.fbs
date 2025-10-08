#write a program to convert days into years,weeks and days
n= int(input(" Enter number of days : "))

#calculate year, week , days

total_years = n//365
remaining_days = n % 365
weeks = remaining_days // 7
days = remaining_days // 7

print(f"\n{n} days = {total_years} year(s), {weeks} week(s), and {days} day(s)")

#write programme to reverse three-digit programme
num = 123
num2 = num

d1 = num2 % 10
num2 = num2 //10

d2 = num2 % 10
num2 = num2 //10

d3 = num2 % 10
num2 = num2 //10

reversed_num = d1 *100 + d2 * 10 + d3

print(f'Reversed number of {num} is {reversed_num}')

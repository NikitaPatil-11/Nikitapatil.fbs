#find max min number

def find_max_min(numbers):
    max_val = numbers[0]  #assumr 1st ele is max
    min_val = numbers[0]   #assume 1st ele is min
    
    for num in numbers:
        if num > max_val:
            max_val = num
            
        if num < min_val:
            min_val = num
            
    return max_val , min_val


#main code
nums=[12,80,50,4,6,7,100]

maximum, minimum = find_max_min(nums)

print("Maximum number:" , maximum)   
print("Minimum number:",minimum)         

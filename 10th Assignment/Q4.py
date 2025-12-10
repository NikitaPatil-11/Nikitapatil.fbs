#reverse the list



#method1
li = [10, 20, 30, 40, 50]
rev = []

for i in range(len(li)-1, -1, -1):
    rev.append(li[i])

print("Reversed List:", rev)


#method2
li = [10, 20, 30, 40, 50]

li.reverse()

print("Reversed List:", li)


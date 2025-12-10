#write a pattern program (incremental)
x = 1
for i in range(1,6):
    for j in range(1 , i+1):
        print(x,end=' ')
        x +=1
    print()
    
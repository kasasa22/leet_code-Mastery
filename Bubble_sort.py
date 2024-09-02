#Bubble sort in ascending order

numbers= [55,13,45,75,9,10,100,3,1]

n = len(numbers)

for i in range(n-1):
    for j in range(n-i-1):
        if numbers[j] >numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print('Sorted array in Acending order is:' , numbers)


#Bubble sort in descending order

for i in range(n-1):
    for j in range(n-i-1):
        if numbers[j] <numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print('Sorted array in decending order is:' , numbers)


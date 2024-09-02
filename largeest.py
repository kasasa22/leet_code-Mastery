numbers= [55,13,45,75,9,10,100,3,1]

maxValue =numbers[0]

for i in numbers:
    if i > maxValue:
        maxValue = i

print("Maximum value in the list is:", maxValue)
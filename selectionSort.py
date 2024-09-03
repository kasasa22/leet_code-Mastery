numbers= [55,13,45,75,9,10,100,3,1]

n = len(numbers)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    min_value = numbers.pop(min_index)
    numbers.insert(i, min_value)

print ("Sorted Values: " ,numbers)


my_array = [64, 34, 25, 12, 22, 11, 90, 5]

s = len(my_array)

for i in range(s):
    min_index = i
    for j in range(i+1, s):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print ("Sorted array: ", my_array)
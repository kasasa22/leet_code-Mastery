def cubic_numbers(numbers):
    sq_numbers = []
    for n in numbers:
      sq_numbers.append(n*n*n)
    return sq_numbers


numbers =[1,2,3,4.5]

print(cubic_numbers(numbers))


for i in range (len(numbers)):
   if numbers[i] ==4:
      print (i)



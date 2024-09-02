import array as arr

nums = arr.array('i', [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10])

print ('create array: ' , end= '')

for i in range(len(nums)):
    print(nums[i] , end='')

nums.pop(2)

print ('After Poping: ' , end='')

for i in range(len(nums)):
    print(nums[i] , end='')





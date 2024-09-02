class Solution(object):
    def twoSum(self, nums, target):
        example ={}

        for i, num in enumerate(nums):
            difference = target-num

            if difference in example:
                return[example[difference],i]
            example[num] = i


solution = Solution()

nums= [2,7,11,15]
target = 9
print(solution.twoSum(nums,target)) 

#count pairs
# space and time complexity O(n) , O(n):

def countPairs(numbers, target):
    set_numbers= set()
    n = len(numbers)
    count_pairs = 0
    pairs = []

    for i in range(n):
        required_num = target - numbers[i]

        if required_num in set_numbers:
            count_pairs += 1
            pairs.append((required_num, numbers[i]))
        set_numbers.add(numbers[i])
    print("Pairs:", pairs)
    
    return count_pairs
numbers=[1,-1,7,5,9,11]
target = 6

print(countPairs(numbers, target))  

#Time and Space Complexity O(nlogn),O(1)

def countPairsSorted(numbers, target):
    numbers.sort()
    n = len(numbers)
    left = 0
    right = n - 1
    count_pairs = 0
    pairs = []

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            count_pairs += 1
            left += 1
            right -= 1
            
        elif current_sum>target:
            right -= 1
        else:
            left += 1
    return count_pairs

numbers=[1,-1,7,5,9,11]

target = 6

print(countPairsSorted(numbers, target))
    
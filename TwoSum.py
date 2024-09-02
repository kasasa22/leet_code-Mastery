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
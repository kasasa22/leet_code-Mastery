/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(let i= 0; i<nums.length;i++){
        for (let j = i+1; j<nums.length;j++){
            if(nums[i]+nums[j]===target){
                return [i,j]
            }

        }
        
    }
    return 1;
    
};

nums = [2,7,11,15]
const result = twoSum(nums,9);
console.log(result);

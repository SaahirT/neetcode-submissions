class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            secondNum = target - nums[i]
            for j in range(len(nums)):
                if j > i and nums[j] == secondNum:
                    return [i, j]
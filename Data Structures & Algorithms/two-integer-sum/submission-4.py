class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []
        for i in range(len(nums)):
            x = target - nums[i]
            for j in range(len(nums)):
                if i !=j and nums[j] == x:
                    list.append(i)
                    list.append(j)
                    return list
            
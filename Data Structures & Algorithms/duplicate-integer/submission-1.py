class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        sum = 0
        T = True
        for i in nums:
            if i not in dict:
                dict[i] = 0
            dict[i] += 1 
            while dict[i] > 1:
                return T
        return not T



        
        
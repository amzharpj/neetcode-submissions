class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            prefix = 1
            postfix = 1
            for j in range(0,i):
                prefix *= nums[j]
            for j in range(i+1,len(nums)):
                postfix *= nums[j]
            output.append(prefix*postfix)
        return output


        


        
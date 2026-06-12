class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        fixed = sorted(set(nums))
        count = 1
        longest = 1
        for i in range(len(fixed)-1):
            if fixed[i]+1 == fixed[i+1]:
                count += 1
            else:
                longest = max(longest,count)
                count = 1
        longest = max(longest,count)
        return longest


            

        
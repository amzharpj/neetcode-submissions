class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        list = []
        for i in nums:
            key = i
            if key not in output:
                output[key] = 0
            output[key] += 1
        for i in range(k):
            temp = ''
            for key in output:
                if output[key] == max(output.values()):
                    temp = key
            list.append(temp)
            del output[temp]
        return list
            


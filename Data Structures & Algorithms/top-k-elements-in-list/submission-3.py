class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = defaultdict(int)
        list = []
        for i in nums:
            output[i] += 1
        for i in range(k):
            temp = ''
            for key in output:
                if output[key] == max(output.values()):
                    temp = key
            list.append(temp)
            del output[temp]
        return list
            


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        helps = {}
        helpt = {}
        for i in s:
            if i not in helps:
                helps[i]=0
            helps[i] += 1
        for i in t:
            if i not in helpt:
                helpt[i]=0
            helpt[i] += 1
        return helps == helpt
        

        
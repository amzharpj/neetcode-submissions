class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for i in strs:
            key =''.join(sorted(i))
            if key not in output:
                output[key]=[]
            output[key].append(i)
        return list(output.values())
        

        


                

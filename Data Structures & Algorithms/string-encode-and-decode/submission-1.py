class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for i in strs:
            encoded += str(len(i))+'#'+i
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            # 1. read full number
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # 2. move to start of word
            i = j + 1
            # 3. build word (YOUR METHOD)
            word = ''
            for k in range(i, i + length):
                word += s[k]

            decoded.append(word)

            # 4. move pointer
            i = i + length
        return decoded

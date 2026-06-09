class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        productall = 1
        countzero = 0
        for i in nums:
            productall =  productall * i
            if i != 0:
                product =  product * i
            else:
                    countzero += 1
        if countzero >= 2:
            product = 0
        for i in nums:
            if i == 0:
                output.append(int(product))
            else:
                others = productall/i
                output.append(int(others))
        return output


        
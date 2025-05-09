class Solution:
    def sortEvenOdd(self, nums):
        even = sorted([nums[i] for i in range(0, len(nums), 2)])
        odd = sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True) 

        result = []
        e = o = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even[e])
                e += 1
            else:
                result.append(odd[o])
                o += 1
        return result
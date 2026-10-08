class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        longest_count = 0
        for i in nums:
            if i == 0:
                longest_count = max(counter, longest_count)
                counter = 0
            else:
                counter += 1
        return max(longest_count, counter)

        
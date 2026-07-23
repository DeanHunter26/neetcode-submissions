class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter_of_ones = 0
        max_consecutive_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter_of_ones += 1
                continue
            else:
                if counter_of_ones > max_consecutive_ones:
                    max_consecutive_ones = counter_of_ones
                counter_of_ones = 0
        if counter_of_ones > max_consecutive_ones:
            return counter_of_ones
        return max_consecutive_ones
            

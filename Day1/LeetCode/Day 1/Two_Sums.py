
import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_map = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in numbers_map:

                return [numbers_map[complement], i]
            numbers_map[num] = i

        return []

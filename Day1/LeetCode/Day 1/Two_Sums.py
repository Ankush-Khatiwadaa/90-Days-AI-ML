from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store number → index mapping
        numbers_map = {}

        # Loop through the list
        for i, num in enumerate(nums):
            # Calculate the number we need to find
            complement = target - num

            # Check if complement already exists in the map
            if complement in numbers_map:
                # If found, return the index of complement and current index
                return [numbers_map[complement], i]

            # If not found, store the number with its index
            numbers_map[num] = i

        # This line is just for safety — problem says one solution always exists
        return []

# 🧪 Sample Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.twoSum([2, 7, 11, 15], 9))   # Output: [0, 1]
    print(solution.twoSum([3, 2, 4], 6))        # Output: [1, 2]
    print(solution.twoSum([3, 3], 6))           # Output: [0, 1]
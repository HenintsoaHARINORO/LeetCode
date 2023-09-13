"""
https://leetcode.com/problems/find-k-closest-elements/description/
"""
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        abs_diff = [(abs(num - x), num) for num in arr].sort()
        nearest_neighbors = abs_diff[:k]
        result = sorted([neighbor[1] for neighbor in nearest_neighbors])

        return result


# Example usage
arr = [1, 2, 3, 4, 5]
k = 4
x = 3

solution = Solution()
result = solution.findClosestElements(arr, k, x)

print(" Nearest Neighbors:", result)

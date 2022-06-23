from typing import List
import sys

class Solution:
    def threeSum(self, nums: List[int], target) -> int:
        results = []
        nums.sort()
        max_val = float('-inf')
        for i in range(len(nums) - 2):
            # 간격을 좁혀가며 합 `sum` 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum <= target:
                    max_val = max(max_val, sum)
                    left += 1
                elif sum > target:
                    right -= 1

        return max_val

n, target = map(int,sys.stdin.readline().split())
*nums, = map(int,sys.stdin.readline().split())
black_jack=Solution()

print(black_jack.threeSum(nums,target))

# 4Sum
Given an array `nums` of *n* integers and an integer `target`, are there elements *a, b, c,* and *d* in `nums` such that *a + b + c + d* = `target`? Find all unique quadruplets in the array which gives the sum of `target`.
#### Note:
The solution set must not contain duplicate quadruplets.
#### Example:
```
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```
## Solution 1. Two Pointers
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k):
            result = []
            if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
                return result
            
            if k == 2:
                return twoSum(nums, target)
            
            for ii in range(len(nums)):
                if ii == 0 or nums[ii - 1] != nums[ii]:
                    for _, sset in enumerate(kSum(nums[ii + 1:], target - nums[ii], k - 1)):
                        result.append([nums[ii]] + sset)
            return result
        
        def twoSum(nums, target):
            result = []
            lo, hi = 0, len(nums) - 1
            while (lo < hi):
                ssum = nums[lo] + nums[hi]
                if ssum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif ssum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    result.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return result
        
        nums.sort()
        return kSum(nums, target, 4)
```
- Time Complexity: `O(n log(n))` for `sort`, `O(n^(k-1))` for recursion.  
If `k == 2`, then `sort` dominates so `O(n log(n))`.  
Else if `k > 2`, then recursion dominates so `O(n^(k-1))`.
- Space Complexity: `O(n)`. We need `O(k)` space for `k` recursions. The worst case `O(n)` is when `k == n`.
## Solution 2. Hashmap
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k):
            if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
                return []
            
            if k == 2:
                return twoSum(nums, target)
            
            result = []
            for ii in range(len(nums)):
                if ii == 0 or nums[ii - 1] != nums[ii]:
                    for _, sset in enumerate(kSum(nums[ii + 1:], target - nums[ii], k - 1)):
                        result.append([nums[ii]] + sset)
            return result
        
        def twoSum(nums, target):
            result = []
            ss = set()
            for ii in range(len(nums)):
                # 1st condition gives opportunity to find the first appearing pair.
                # 2nd condition prevents duplicates.
                if len(result) == 0 or result[-1][1] != nums[ii]:
                    if target - nums[ii] in ss:
                        result.append([target - nums[ii], nums[ii]])
                ss.add(nums[ii])
            return result
        
        nums.sort()
        return kSum(nums, target, 4)
```
- Time Complexity: `O(n log(n))` for `sort`, `O(n^(k-1))` for recursion.  
If `k == 2`, then `sort` dominates so `O(n log(n))`.  
Else if `k > 2`, then recursion dominates so `O(n^(k-1))`.
- Space Complexity: `O(n)` for the hashmap. Recursion needs at most `O(n)` space.

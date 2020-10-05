# Two Sum
Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.  
You may assume that each input would have ***exactly one solution***, and you may not use the *same* element twice.  
You can return the answer in any order.

#### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```
#### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
#### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
#### Constraints:
- 2 <= nums.length <= 105
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.

## Solution 1. Two Pointers
Need to modify to return indices.
```python
class Solution:
    def twoSum(nums, target):
        nums.sort()
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
```
- Time Complexity: `O(n)`.
- Space Complexity: `O(1)`.
## Solution 2. Hashmap
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for ii in range(len(nums) - 1):
        hashmap[nums[ii]] = ii
        newt = target - nums[ii + 1]
        if newt in hashmap:
            return [hashmap[newt], ii + 1]
```
- Time Complexity: `O(n)`.
- Space Complexity: `O(n)` for hashmap.

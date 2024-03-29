"""
698. Partition to K Equal Sum Subsets

https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
"""


def canPartitionKSubsets(nums: list[int], k: int) -> bool:
    sub_size = sum(nums)/k
    if round(sub_size) != sub_size:
        return False

    nums.sort()
    subsets = [0]*k

    return build_sets(subsets, nums, sub_size)


def build_sets(subsets: list, nums: list, sub_size: int) -> bool:
    if not nums:
        return True

    num = nums.pop()
    for i in range(len(subsets)):
        if num <= sub_size - subsets[i]:
            subsets[i] += num
            if build_sets(subsets, nums, sub_size):
                return True
            subsets[i] -= num
            if subsets[i] == 0:
                break

    nums.append(num)
    return False

if __name__ == '__main__':
    print(canPartitionKSubsets([2,2,2,2,3,4,5], 4))

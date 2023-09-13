"""
454. 4Sum II
https://leetcode.com/problems/4sum-ii

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

"""


from collections import Counter


# The fast way, O(n^2)
def fourSumCount(nums1: list[int], nums2: list[int], nums3: list[int],
                 nums4: list[int]) -> int:
    nums1_counts = Counter(nums1)
    nums2_counts = Counter(nums2)
    nums3_counts = Counter(nums3)
    nums4_counts = Counter(nums4)

    counts12 = Counter()
    for num1, count1 in nums1_counts.items():
        for num2, count2 in nums2_counts.items():
            counts12[num1 + num2] += count1 * count2

    count_total = 0
    for num3, count3 in nums3_counts.items():
        for num4, count4 in nums4_counts.items():
            count_total += counts12[-num3 - num4] * count3 * count4

    return count_total


print(fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]))
print(fourSumCount(nums1=[0], nums2=[0], nums3=[0], nums4=[0]))


# Slower, O(n^3)
def fourSumCount2(nums1: list[int], nums2: list[int], nums3: list[int],
                  nums4: list[int]) -> int:
    nums1_counts = Counter(nums1)
    nums2_counts = Counter(nums2)
    nums3_counts = Counter(nums3)
    nums4_counts = Counter(nums4)

    count_total = 0
    for num1 in nums1_counts:
        count1 = nums1_counts[num1]
        for num2 in nums2_counts:
            count2 = nums2_counts[num2]
            for num3 in nums3_counts:
                target = -num1 - num2 - num3
                if target in nums4_counts:
                    count_total += count1 * count2 * nums3_counts[num3]\
                        * nums4_counts[target]

    return count_total


print(fourSumCount2(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]))
print(fourSumCount2(nums1=[0], nums2=[0], nums3=[0], nums4=[0]))

"""
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2 = nums2, nums1
        m, n = n, m

    l1 = 0
    r1 = m
    
    while l1 <= r1:
        # these are indexes of right pointers
        mid1 = r1 - (r1 - l1 + 1) // 2
        mid2 = (m + n + 1) // 2 - mid1
    
        vall1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
        valr1 = float('inf') if mid1 == m else nums1[mid1]
        vall2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
        valr2 = float('inf') if mid2 == n else nums2[mid2]

        if vall1 <= valr2 and vall2 <= valr1:
            if (m + n) % 2 == 1:
                return max(vall1, vall2)
            else:
                return (min(valr1, valr2) + max(vall1, vall2)) / 2
        elif vall2 > valr1:
            l1 = mid1 + 1
        else:
            r1 = mid1 - 1
    return -1


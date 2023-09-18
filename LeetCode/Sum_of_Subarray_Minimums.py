"""
907. Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums

Given an array of integers arr, find the sum of min(b), where
b ranges over every (contiguous) subarray of arr. Since the answer
may be large, return the answer modulo 10^9 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444

Constraints:

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4

"""


# Method 1, O(n^2), time limit exceeded:
# Use divide and conquer, finding the minimum of the array and
# splitting on either side of it during each recursive call
# Worst-case example: a monotonically incrasing array
def sumSubarrayMins(arr: list[int]) -> int:
    modulo = 10**9 + 7
    result = 0

    def helper(left: int, right: int) -> None:
        nonlocal result
        if left > right:
            return
        elif left == right:
            to_add = arr[left]
            result += to_add
            result %= modulo
            return

        min_idx = min(range(left, right + 1), key=lambda i: arr[i])
        n = right - left + 1
        all_subs = (n * (n + 1)) // 2
        n = min_idx - left
        left_subs = (n * (n + 1)) // 2
        n = right - min_idx
        right_subs = (n * (n + 1)) // 2
        mult = all_subs - left_subs - right_subs
        to_add = (arr[min_idx] * mult) % modulo
        result += to_add
        result %= modulo

        helper(left, min_idx - 1)
        helper(min_idx + 1, right)

    helper(0, len(arr) - 1)
    return result


print(sumSubarrayMins([3, 1, 2, 4]))
print(sumSubarrayMins([11, 81, 94, 43, 3]))


# Method 2, O(n * log(n)) due to sorting:
# We use intervals.
# Realize that the we can go through the numbers in reverse order, joining
# intervals and counting the number of subarrays in each new/expanded interval.
MODULO = 10**9 + 7


def sumSubarrayMins2(arr: list[int]) -> int:
    ordered = []
    for i, num in enumerate(arr):
        ordered.append((num, i))
    ordered.sort(reverse=True)

    intervals = {}

    result = 0
    for num, i in ordered:
        if i-1 in intervals and i+1 in intervals:
            left = intervals.pop(i-1)
            right = intervals.pop(i+1)
        elif i-1 in intervals:
            left = intervals.pop(i-1)
            right = i
        elif i+1 in intervals:
            left = i
            right = intervals.pop(i+1)
        else:
            left = right = i

        intervals[left] = right
        intervals[right] = left
        result += (i - left + 1) * (right - i + 1) * num
        result %= MODULO

    return result


print(sumSubarrayMins2([3, 1, 2, 4]))
print(sumSubarrayMins2([11, 81, 94, 43, 3]))


# Method 3, O(n):
# This method uses a dynamic programming model.
# It uses a monotonically increasing stack with a dynamic programming table.
MODULO = 10**9 + 7


def sumSubarrayMins3(arr: list[int]) -> int:
    stack = []
    dp = [0] * len(arr)

    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] > num:
            stack.pop()

        if stack:
            smaller_left = stack[-1]
            # the way we add on from the previous DP reference
            # properly counts the number of subarrays
            dp[i] = (dp[smaller_left] + num * (i - smaller_left))
        else:
            dp[i] = num * (i + 1)

        stack.append(i)

    return sum(dp) % MODULO


print(sumSubarrayMins3([3, 1, 2, 4]))
print(sumSubarrayMins3([11, 81, 94, 43, 3]))

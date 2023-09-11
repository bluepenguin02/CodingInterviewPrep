"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of
all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:
* 2 <= nums.length <= 105
* -30 <= nums[i] <= 30
* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count
as extra space for space complexity analysis.)
"""

# better solution
def productExceptSelf(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return [0]
            
    prod = [0] * len(nums)
    prod[-1] = nums[-1]
    for i in reversed(range(1, len(nums)-1)):
        prod[i] = nums[i]*prod[i+1]
    prod[0] = prod[1]
    cumprod = nums[0]
    for i in range(1, len(nums)-1):
        prod[i] = cumprod * prod[i+1]
        cumprod *= nums[i]
    prod[-1] = cumprod
    
    return prod

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))

# OK solution
from functools import reduce
import operator

def productExceptSelf2(nums: list[int]) -> list[int]:
    oput = [1]*len(nums)

    last_zero = 0
    for i, num in enumerate(nums):
        if num == 0:
            last_zero = i
    
    prefix = 1
    suffix = 0
    prev = nums[0]
    for i, num in enumerate(nums[1:]):
        if i == last_zero:
            suffix = reduce(operator.mul, nums[i+1:])
        oput[i] = prefix * suffix
        prefix *= prev
        prev = num
        if i >= last_zero:
            suffix //= num
        
    if suffix == 0:
        suffix = 1
    oput[-1] = prefix * suffix
        
    return oput

print(productExceptSelf2([1,2,3,4]))
print(productExceptSelf2([-1,1,0,-3,3]))
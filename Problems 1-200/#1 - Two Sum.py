# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

========

# MR CHAN'S SOLUTION using while loop(24/8/22)

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        done = False 
        counter = 0
        needed_index = None
        while not done:
            needed_number = target - nums[counter]
            if needed_number in nums:
                needed_index = nums.index(needed_number)
                if needed_index != counter:
                    done = True
                else:
                    counter += 1
            else:
                counter += 1
        return [counter, needed_index]

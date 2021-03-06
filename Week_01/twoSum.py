# 1. 两数之和
# https://leetcode-cn.com/problems/two-sum/

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

# 示例:

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 暴力法：
class Solution:
    def (self, nums: list, target: int) -> list:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i , j]

s = Solution()
print(s.([21,7,11,15], 36))
# 输出： [0, 3]

# 由于还没认真学习哈希表，以后添加使用哈希表的方法！
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        it = 1
        result = []
        
        for i in range(len(nums)):
            for j in range(it, len(nums)):
                if(nums[i] + nums[j] == target):
                    result.append(i)
                    result.append(j)
                    break
            it += 1
            if(len(result) != 0):
                break
        return result

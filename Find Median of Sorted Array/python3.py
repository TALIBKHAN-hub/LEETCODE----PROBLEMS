class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged_list = nums1 + nums2
        merged_list.sort()
        
        if (len(merged_list) % 2 == 1):
            return merged_list[(len(merged_list)//2)]
            
        else:
            val1 = merged_list[(len(merged_list)//2)-1]
            val2 = merged_list[(len(merged_list)//2)]
            return (val1 + val2)/2

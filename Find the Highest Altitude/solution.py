class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alti_list = [0,]
        current = 0

        for altitude in gain:
            current += altitude
            alti_list.append(current)
            
        return max(alti_list)

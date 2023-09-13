class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxseenright = 0
        maxseenright_arr = [0]*len(height)
        maxseenleft = 0
        rainwater = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > maxseenright:
                maxseenright_arr[i] = height[i]
                maxseenright = height[i]
            else:
                maxseenright_arr[i] = maxseenright
        for i in range(0, len(height)):
            rainwater = rainwater + max(min(maxseenright_arr[i],
            maxseenleft) - height[i],0)
            if height[i] > maxseenleft:
                maxseenleft = height[i]
        return rainwater

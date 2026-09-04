class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0 
        if n == 0:
            return 0
        maxL = [0] * n
        maxR = [0] * n
        # prefix 
        maxL[0] = height[0]
        for i in range(1,n):
            maxL[i] = max(maxL[i-1] , height[i])
        
        # suffix
        maxR[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            maxR[i] = max(maxR[i+1] , height[i])
       
        for i in range(0,n):
            current_i = min(maxL[i],maxR[i]) - height[i]
            total += current_i
        return total
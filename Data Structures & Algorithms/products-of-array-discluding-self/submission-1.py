class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
            # prefix.append(prefix[i-1] * nums[i])

        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            # suffix.append(suffix[i + 1] * nums[i])
            suffix[i]=suffix[i+1]*nums[i]

        res = []
        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 1
            right = suffix[i + 1] if i < n - 1 else 1
            ans = left * right
            res.append(ans)
        return res

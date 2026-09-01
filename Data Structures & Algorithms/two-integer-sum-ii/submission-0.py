class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1

        while left < right:
            sum = numbers[left] + numbers[right]
            # check the sum againts target
            if (sum == target):
                return [left + 1 , right +1]
            if sum < target:
                left += 1
            else: right -=1
            sum =0 

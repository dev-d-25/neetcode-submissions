class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        lowerS = s.lower()
        left = 0
        right = n-1
        flag = True


        while left < right:
            # lowerSkip non ilowerS alnum itemlowerS
            if lowerS[left].isalnum() == False: 
                left +=1 
                continue
            if lowerS[right].isalnum() == False: 
                right -=1 
                continue

            if lowerS[left] != lowerS[right]:
                flag = False
                break
            else:
                left +=1
                right -=1

        return flag
            
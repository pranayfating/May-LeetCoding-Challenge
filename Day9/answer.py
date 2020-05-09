class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        
        if num == 1:
            return True
        while(left!=right):
            mid = int(left+right)/2
            if mid == left:
                return False
            sq = mid*mid
            if sq == num:
                return True
            elif sq < num:
                left = mid
            else:
                right = mid
        return False

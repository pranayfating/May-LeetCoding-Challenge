class Solution:

        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n-1
        
        for i in range(n):
            m = int((l+r)/2)
            
            
            if(isBadVersion(m+1)):
               
                if l==r:
                    return m+1
                r = m
            else:
                if l==m:
                    l = m+1
                else:
                    l=m
        return -1

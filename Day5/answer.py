class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s=="":
            return -1
        for i in range(len(s)):
            if i==0:
                if s[i] not in s[i+1:]:
                    return i
            elif i==len(s)-1:
                if s[i] not in s[:i]:
                    return i
            else:
                if s[i] not in s[i+1:] and s[i] not in s[:i]:
                    return i
        return -1
        

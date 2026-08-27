class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub_len = 0
        window = set()
        for i in range(len(s)):
            if s[i] in window: 
                while s[i] in window: 
                    window.remove(s[l])
                    l += 1
                window.add(s[i])
                sub_len = max(sub_len,i-l + 1)
            else: 
                window.add(s[i])
                sub_len = max(sub_len,i-l + 1)
        
        return sub_len




        


            
            
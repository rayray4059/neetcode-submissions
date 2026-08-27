class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = {}
        counts1 = {}
        m = len(s1)
        l = 0
        
        for i in range(len(s1)):
            if s1[i] not in counts1:
                counts1[s1[i]] = 1
            else: 
                counts1[s1[i]] += 1

        for r in range(len(s2)):
            if s2[r] not in counts:
                counts[s2[r]] = 1
            else: 
                counts[s2[r]] += 1

            windowLen = r - l + 1
            if windowLen > m:
                counts[s2[l]] -= 1
                if counts[s2[l]] == 0: del counts[s2[l]]
                l += 1
                windowLen -= 1
            
            if windowLen == m and counts == counts1:
                return True

        return False





class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        best_length = 0
        l = 0

        for r in range(len(s)):
            
            if s[r] not in counts:
                counts[s[r]] = 1
            else: 
                counts[s[r]] += 1
            
            windowSize = r - l + 1
            mostFreq = max(counts.values())
            numReps = windowSize - mostFreq
            if numReps > k:
                while numReps > k:
                    counts[s[l]] -= 1
                    l += 1
                    windowSize = r - l + 1
                    mostFreq = max(counts.values())
                    numReps = windowSize - mostFreq
                
                best_length = max(best_length, r - l + 1)
            else:
                best_length = max(best_length, r - l + 1)
        
        return best_length
            



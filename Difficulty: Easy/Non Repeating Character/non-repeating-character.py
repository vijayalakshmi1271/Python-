class Solution:
    def nonRepeatingChar(self,s):
        freq = [0] * 26  
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in s:
            if freq[ord(ch) - ord('a')] == 1:
                return ch
        return '$'

    
    
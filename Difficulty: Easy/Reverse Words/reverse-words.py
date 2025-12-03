class Solution:
    def reverseWords(self, s):
        words = [w for w in s.split('.') if w]   
        words.reverse()                     
        return ".".join(words)                   

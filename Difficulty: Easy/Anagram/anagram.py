class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
            
        hashmap = {}
        
        for i in s1:
            hashmap[i] = hashmap.get(i, 0) + 1
            
        for i in s2:
            if i not in hashmap:
                return False
                    
            hashmap[i] -= 1
                
            if hashmap[i] < 0:
                return False
                
        return True
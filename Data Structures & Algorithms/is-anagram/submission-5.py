class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if len(s) == len(t): 
            #if sorted(s) == sorted(t): 
               # return True; 
        #return False; 
        if len(s) != len(t):
            return False 

        countS = {}
        countT = {}

        for c in s: 
            if c in countS: 
                countS[c] = countS[c] + 1
            else: 
                countS[c] = 1
        
        for x in t: 
            if x in countT:  
                countT[x] = countT[x] + 1
            else: 
                countT[x] = 1
        
        if countS == countT:
            return True 
        return False 
            

                

        

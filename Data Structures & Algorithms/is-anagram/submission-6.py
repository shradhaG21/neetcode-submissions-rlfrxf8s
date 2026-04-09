class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if len(s) == len(t): 
            #if sorted(s) == sorted(t): 
               # return True; 
        #return False; 
       
       if len(s) != len(t): #First check this because if the string do not have the same length they are automatially not anagrams 
            return False 
        
       countS = {} #create a hashmap for string s so that we store characters and their frequencies 
       countT = {} #create a hashmap for string t so that we can store characters and their frequencies 

       for c in s: #For every character in string s
            if c in countS: #If the character has been seen before in the hashmap 
                countS[c] = countS[c] + 1 #Update the current frequency value by adding 1 
            else: #Otherwise if it has not been seen before 
                countS[c] = 1 #The count of that character will equal one 
        
       for x in t: #For every character in string t 
            if x in countT: #If the character has been seen before in the hashmap or present in the dictionaty 
                countT[x] = countT[x] + 1 #Update the count of the specific character by adding 1
            else: 
                countT[x] = 1 #Otherwise if it has not been seen before then character count will be 1 
        
       if countS == countT: 
            return True 
       return False 

            

                

        

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      # nums.sort()# Sort the array first so duplicates are next to each other 
      # for i in range (0, len(nums) - 1): #Do len(nums) - 1 because when we get to the next line we will already get to the last index 
       # if (nums[i] == nums[i+1]): # Compare the value at the current index to the next index. This should work because the sort function has alrready grouped the same values next to each other. 
         #   return True #If there are duplicates, return true
       # return False #If not return false. 


       seen = set() #Start off with an empty set 
       for i in range (0, len(nums)): #loop through the list 
        if nums[i] not in seen: 
            seen.add(nums[i])
        else: 
            return True
       return False 


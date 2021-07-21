#%%
class Solution:
    
    def checkPrime(self, num: int) -> bool:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    return True
        return False
    
    def goodNum(self, n:int) -> bool:
        #check if even index is even
        #check if odd index is prime
        #if complete number is "good" then return true
        #first occurance of bad return false
        
        index = 0
        chNum = str(n)
        good = False
        for i in chNum:
            if int(i) % 2 == 0 and index % 2 == 0:
                good = True
            elif(self.checkPrime(int(i)) and index % 2 != 0):
                good = True
            else:
                return False
            
        return good
            
    def countGoodNumbers(self, n: int) -> int:
        #generate all numbers of n length
        #n = 1, 0-9
        #n = 2, 0-99
        #n = 3, 0-999
        nums = "9"*n
        str(nums)
        print(nums)
        nums = int(nums)
        count = 0
        for i in range(nums):
            if(self.goodNum(i)):
                count = count + 1
                
        print(count)
        return count

        
    countGoodNumbers(0,1)

    
# %%

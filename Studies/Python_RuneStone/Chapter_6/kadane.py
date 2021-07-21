def maxSubArraySum(self,a,size):
    
    #loop through list
    #if sum is negative or 0 reset sum to next index
    if size < 1:
        return 0
        
    current_sum = 0
    max_sum = 0
    i = 0
    
    while i < size:
        #if current_sum <= 0 and i+1 < size:
        #   current_sum = a[i + 1]
        
        current_sum = current_sum + a[i]
        if current_sum <= 0:
            current_sum = a[i]
        
        print("Current ",current_sum)
        if current_sum > max_sum:
            max_sum = current_sum
        i = i + 1
        print("max", max_sum)
    return max_sum

max
#find missing number
nums=[2,1,4,0,5,6]
n=len(nums)
expectedSum=n*(n+1)//2
actualSum=0
for i in nums:
    actualSum+=i
print("the missing number is:", expectedSum-actualSum)    

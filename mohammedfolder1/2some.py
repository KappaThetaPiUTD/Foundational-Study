#this gives us the values of the array
nums = [2,7,11,15]
target = 9 #this is the number were trying to reach

for i in range (len(nums)): # this goes through the array and tests each indices to reach 9
    for j in range (len(nums)):
        if nums[i] + nums[j] == target: # if our target is reached print out the index value of where it is found
            print (f"[{i}, {j}]")
        else :
            print ("The code does not equal to the target")
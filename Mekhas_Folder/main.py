#nums array with values inside square brackets
nums = [2, 7, 11, 15]
#target for checking
target = 9

#iterate through all of the elements in array nums with x
for x in range(len(nums)):
    #iterate through all of the elements starting from the index x is at in array nums with y
    for y in range(x,len(nums)): 
        #if the value in the first iteration + value in second iteration equals the target number
        if nums[x] + nums[y] == target:
            #print out the index of those values of the array
            print(f"[{x}, {y}]")

        


nums = [2,8,11,15]
target = 9
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i] + nums[j] == target:
            print(f"[{i} , {j}]")
else:
    print("Try again")

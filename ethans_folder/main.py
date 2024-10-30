nums = [2,7,11,15]
target = 9
# index1 = 0
# for num1 in nums:
#     index2 = 1
#     for num2 in nums[1:]:
#         if num1 + num2 == target:
#             print(index1, index2)
#         index2+=1
#     index1 += 1

"""
0 1  2  3
[2,7,11,15]
   1  2  3
"""

for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i] + nums[j] == target:
            print(f"[{i}, {j}]")


"""
for(int i = 0; i < nums.length; i++){
    for(int j = 1; j < nums.length; j++){
        if(nums[i] + nums[j] == target){
            return [i, j];
        }
    }
}
"""
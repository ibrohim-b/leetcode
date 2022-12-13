nums = [1,2,1,1,2,2,2]
nums = str(nums)
val = 2
val = str(val)
nums = nums.replace(val,"_")
nums = nums.replace(" ","")
print(nums)
nums = nums.replace("[","")
nums = nums.replace(']','')
nums = nums.split(",")
print(nums)
new = []
for i in range(len(nums)-1):
    if nums[i] != "_":
        nums[i] = int(nums[i])
        new.append(nums[i])
for i in nums:
    if i == "_":
        new.append(i)
print(new)

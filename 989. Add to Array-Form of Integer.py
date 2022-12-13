num = [2,7,4]
k = 181
new_list = []
nums = ""
for i in num:
    nums += str(i)
nums = str(int(nums)+k)
for i in range(len(str(nums))):
    new_list.append(int(nums[i]))
print(new_list)
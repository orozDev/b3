nums = [i for i in range(10) if i != 4]

num = 4 if 4 in nums else 3 if 3 in nums else 0

print(nums)
print(num)
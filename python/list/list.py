nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums.append(10)
nums.extend([11, 12, 13, 14, 15])

nums = [*nums, 16, 17, 18, 19, 20]

print(nums[0], nums[-2])

nums.reverse()

nums2 = nums.copy()

nums2.pop()


print(nums)
print(nums2)

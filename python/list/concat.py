nums = [1, 2, 3, 4, 5]

nums.append(6)
nums.extend([7, 8, 10])

nums2 = [11, 12]
nums.extend(nums2)

nums3 = [13, 14, 15, 16]

nums = [1, 2, *nums, 12, 12, 14, *nums3] # nums = nums

print(nums)


names = ['Yntymak', 'Aiperi']
names2 = ['Asat', 'Abduvali']
names3 = ['Ibragim', 'Salahidin']

res = [*names, *names2, *names3]

print(res)


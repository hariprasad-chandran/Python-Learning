# Program to sort a list using bubble sort

def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp


nums = [4, 5, 2, 5, 6, 9, 7, 8]
sort(nums)
print(nums)

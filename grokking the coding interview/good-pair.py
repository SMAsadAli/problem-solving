# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def sol(nums):
    count = {}
    total_pairs = 0
    for value in nums:
        count[value] = count.get(value, 0) + 1
    for value in count.values():
        total_pairs += (value * (value - 1))//2
    return total_pairs


print(sol([1, 2, 3, 1, 1, 3]))  # 4
print(sol([1, 1, 1, 1]))  # 6
print(sol([1, 2, 3]))  # 0

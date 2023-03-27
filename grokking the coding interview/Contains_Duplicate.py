#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.#

def solutionWithLoop(arr):
    arr.sort()
    cur = arr[0]
    for index in range(1, len(arr)):
        if cur == arr[index]:
            return True
        cur = arr[index]
    return False

def solutionWithSet(arr):
    arr_set = set(arr)
    return len(arr) != len(arr_set)

print(solutionWithLoop([1, 2, 3, 1]))
print(solutionWithSet([1, 2, 3, 1]))
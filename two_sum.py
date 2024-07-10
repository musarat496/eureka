def twoSum(nums, target):
    index_of_traversed_numbers = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in index_of_traversed_numbers:
            return [index, index_of_traversed_numbers[complement]]

        index_of_traversed_numbers[num] = index
    return []


result = twoSum([2, 7, 11, 15], 9)
print(result)

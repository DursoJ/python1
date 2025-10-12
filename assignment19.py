"""
Challenge: Implement the sorting algorithm without using any built-in sorting functions.

====================================
Description: Develop a function called sort_list that takes a list of numbers as input and returns a new list containing the same elements sorted in ascending order.
"""

def sort_list(list1):
    if len(list1) <= 1:
        return list1

    mid = len(list1) // 2
    left_half = sort_list(list1[:mid])
    right_half = sort_list(list1[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


nums = [38, 27, 43, 3, 9, 82, 10]
print("Original list:", nums)
print("Sorted list:", sort_list(nums))

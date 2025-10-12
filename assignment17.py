"""
Challenge: Optimize the function to handle large input lists efficiently.

==============================
Description: Develop a function called find_common_elements that takes two lists as input and returns a new list containing elements that are common to both input lists.
"""

def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements

def main():
    list1 = [2, 3, 4, 5, 6, 8, 10]
    list2 = [1, 2, 16, 4, 5, 11, 7, 8, 9, 10]
    print(find_common_elements(list1, list2))

main()
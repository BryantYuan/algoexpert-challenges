def spiralTraverse(array):
    # Write your code here
    return None

# def spiralTraverse(array):
#     result = []
#     if not array:  # Handle empty matrix
#         return result
#
#     # Define the bounds of the spiral traversal
#     top, bottom = 0, len(array) - 1
#     left, right = 0, len(array[0]) - 1
#
#     while top <= bottom and left <= right:
#         # Traverse the top row from left to right
#         for col in range(left, right + 1):
#             result.append(array[top][col])
#         top += 1  # Shrink the top boundary
#
#         # Traverse the right column from top to bottom
#         for row in range(top, bottom + 1):
#             result.append(array[row][right])
#         right -= 1  # Shrink the right boundary
#
#         # Traverse the bottom row from right to left (if applicable)
#         if top <= bottom:
#             for col in range(right, left - 1, -1):
#                 result.append(array[bottom][col])
#             bottom -= 1  # Shrink the bottom boundary
#
#         # Traverse the left column from bottom to top (if applicable)
#         if left <= right:
#             for row in range(bottom, top - 1, -1):
#                 result.append(array[row][left])
#             left += 1  # Shrink the left boundary
#
#     return result
#
# # Test cases
# test_cases = [
#     {"array": [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]],
#      "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]},
#     {"array": [[1]], "expected": [1]},
#     {"array": [[1, 2], [4, 3]], "expected": [1, 2, 3, 4]},
#     {"array": [[1, 2, 3], [8, 9, 4], [7, 6, 5]], "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
#     {"array": [[19, 32, 33, 34, 25, 8], [16, 15, 14, 13, 12, 11], [18, 31, 36, 35, 26, 9], [1, 2, 3, 4, 5, 6],
#                [20, 21, 22, 23, 24, 7], [17, 30, 29, 28, 27, 10]],
#      "expected": [19, 32, 33, 34, 25, 8, 11, 9, 6, 7, 10, 27, 28, 29, 30, 17, 20, 1, 18, 16, 15, 14, 13, 12, 26, 5, 24,
#                   23, 22, 21, 2, 31, 36, 35, 4, 3]},
#     {"array": [[4, 2, 3, 6, 7, 8, 1, 9, 5, 10], [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]],
#      "expected": [4, 2, 3, 6, 7, 8, 1, 9, 5, 10, 14, 11, 17, 13, 18, 20, 16, 15, 19, 12]},
#     {"array": [[27, 12, 35, 26], [25, 21, 94, 11], [19, 96, 43, 56], [55, 36, 10, 18], [96, 83, 31, 94],
#                [93, 11, 90, 16]],
#      "expected": [27, 12, 35, 26, 11, 56, 18, 94, 16, 90, 11, 93, 96, 55, 19, 25, 21, 94, 43, 10, 31, 83, 36, 96]},
#     {"array": [[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]], "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]},
#     {"array": [[1, 2, 3], [12, 13, 4], [11, 14, 5], [10, 15, 6], [9, 8, 7]],
#      "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]},
#     {"array": [[1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 20]],
#      "expected": [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2]},
#     {"array": [[1, 3, 2, 5, 4, 7, 6]], "expected": [1, 3, 2, 5, 4, 7, 6]},
#     {"array": [[1], [3], [2], [5], [4], [7], [6]], "expected": [1, 3, 2, 5, 4, 7, 6]},
# ]
#
# # Running test cases
# for i, test in enumerate(test_cases):
#     output = spiralTraverse(test["array"])
#     assert output == test["expected"], f"Test Case {i + 1} failed: Expected {test['expected']}, but got {output}"
#
# print("All test cases passed!")
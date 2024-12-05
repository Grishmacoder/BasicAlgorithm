"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements are 
in the range [0, 9]. The number of digits in both the numbers cannot differ by 
more than 1. You're not allowed to use any sorting function that Python 
provides and the expected time complexity is O(nlog(n)).

You should implement the function body according to the rearrange_digits 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""

def rearrange_digits(input_list: list[int]) -> tuple[int, int]:
    if not input_list:
        return 0,0

    def merge_sort(input_list):
        if len(input_list) <= 1:
            return input_list

        mid = len(input_list)//2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])

        return merge(left,right)

    def merge(left,right):
        i, j = 0,0
        result = []
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_list = merge_sort(input_list)
    num1 = ""
    num2 = ""
    for index,digit in enumerate(sorted_list):
        if index % 2 == 0:
            num1 += str(digit)
        else:
            num2 += str(digit)

    if not num1:
        num1 = "0"
    if not num2:
        num2 = "0"
    return int(num1), int(num2)


def test_function(test_case: tuple[list[int], list[int]]) -> None:
    output: tuple[int, int] = rearrange_digits(test_case[0])
    solution: list[int] = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    # Edge case: Single element list
    # print(rearrange_digits([9]))
    # test_function(([9], [9, 0]))
    # # Expected output: Pass
    #
    # # Normal case: Mixed positive and negative numbers
    # print(rearrange_digits([4, 6, 2, 5, 9, 8]))
    # test_function(([3, -2, 1, -4, 5], [531, -42]))
    # # Expected output: Pass
    #
    # # Normal case: list with zeros
    # test_function(([0, 0, 0, 0, 0], [0, 0]))
    # # Expected output: Pass
    #
    # # Normal case: list with repeated numbers
    # print(rearrange_digits([2, 2, 2, 2, 2]))
    # test_function(([2, 2, 2, 2, 2], [222, 2]))
    # Expected output: Pass
    test_function(([9], [9, 0]))  # Pass
    test_function(([3, 2, 1, 4, 5], [531, 42]))  # Pass
    test_function(([0, 0, 0, 0, 0], [0, 0]))  # Pass
    test_function(([2, 2, 2, 2, 2], [222, 22]))  # Pass
    test_function(([4, 6, 2, 5, 9, 8], [964, 852]))  # Pass
"""
Problem 3: Rearrange Array Elements

Given an input array consisting on only 0, 1, and 2, sort the array in a single
traversal. You're not allowed to use any sorting function that Python provides.

Note that O(n) does not necessarily mean single-traversal. For e.g. if you
traverse the array twice, that would still be an O(n) solution but it will not
count as single traversal.

You should implement the function body according to the sort_012 function
signature. Use the test cases provided below to verify that your algorithm is
correct. If necessary, add additional test cases to verify that your algorithm
works correctly.
"""

def sort_012(input_list: list[int]) -> list[int]:

    left,right = 0, len(input_list)-1
    i=0
    while i <= right:
        if input_list[i] == 0:
            input_list[left],input_list[i] = input_list[i],input_list[left]
            left += 1
        elif input_list[i] == 2:
            input_list[right],input_list[i]= input_list[i],input_list[right]
            right -= 1
            i -= 1
        i+=1


    return input_list

def test_function(test_case: list[list[int]]) -> None:

    sorted_array: list[int] = sort_012(test_case[0])
    print(sorted_array)
    if sorted_array == sorted(test_case[0]):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    # Edge case: Empty input list
    test_function([[]])
    # Expected output: Pass

    # Normal case: Mixed elements
    test_function([[0, 1, 2, 0, 1, 2]])
    # Expected output: Pass

    # Normal case: Already sorted list
    test_function([[0, 0, 1, 1, 2, 2]])
    # Expected output: Pass

    # Normal case: Reverse sorted list
    test_function([[2, 2, 1, 1, 0, 0]])
    # Expected output: Pass


def rotated_array_search(input_list: list[int], number: int) -> int:
    left, right = 0, len(input_list)-1
    while left <= right:
        mid = (left+right) //2
        if number == input_list[mid]:
            return mid
        if input_list[left] <= input_list[mid]:    #left sorted portion
            if number > input_list[mid] or number < input_list[left]:
                left = mid +1
            else:
                right= mid -1
        else:                                         #Right sorted portion
            if number < input_list[mid] or number > input_list[right]:
                right = mid -1
            else:
                left= mid + 1
    return -1


# Test function using provided test cases
def test_function(test_case: list[list[int], int]) -> None:
    input_list: list[int] = test_case[0]
    number: int = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

def linear_search(input_list: list[int], number: int) -> int:

    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

if __name__ == '__main__':
    # Edge case: Empty input list
    test_function([[], 5])
    # Expected output: Pass

    # Normal case: Number at the beginning of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 4])
    # Expected output: Pass

    # Normal case: Number at the end of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 2])
    # Expected output: Pass

    # Normal case: Number in the middle of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 6])
    # Expected output: Pass

def sqrt(number: int) -> int:

    left,right = 0, number
    res = 0
    while left <= right:
        mid = (left+(right-left)//2)
        if mid**2 > number:
            right = mid -1
        elif mid**2< number:
            left = mid+1
            res = mid
        else:
            return mid
    return res



if __name__ == "__main__":
    # Test cases
    print("Pass" if 3 == sqrt(9) else "Fail")   # Expected Output: Pass
    print("Pass" if 0 == sqrt(0) else "Fail")   # Expected Output: Pass
    print("Pass" if 4 == sqrt(16) else "Fail")  # Expected Output: Pass
    print("Pass" if 1 == sqrt(1) else "Fail")   # Expected Output: Pass
    print("Pass" if 5 == sqrt(27) else "Fail")  # Expected Output: Pass

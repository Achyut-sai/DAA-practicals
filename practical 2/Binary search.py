import time


def binary_search(arr, target):
    """Performs Iterative Binary Search on a sorted list.

    Time Complexities:
      - Best Case: O(1)       -> Target is the middle element on iteration 1.
      - Average Case: O(log n)-> Search space halves on each step.
      - Worst Case: O(log n)  -> Target requires maximum divisions or is absent.

    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# 1. User Input
try:
    user_input = input("Enter space-separated numbers: ")
    arr = [int(x) for x in user_input.split()]

    # Binary search requires sorted data
    arr.sort()
    print(f"Sorted input array: {arr}")

    target = int(input("Enter target number to search: "))

    # 2. Measure Execution Time
    start_time = time.perf_counter()
    result = binary_search(arr, target)
    end_time = time.perf_counter()

    # 3. Display Results
    execution_time_ms = (end_time - start_time) * 1000

    if result != -1:
        print(f"\n[Result]: Target {target} found at index {result} (in sorted array).")
    else:
        print(f"\n[Result]: Target {target} not found in the array.")

    print(f"Execution Time: {execution_time_ms:.6f} ms")

except ValueError:
    print("Invalid input! Please enter valid integers.")
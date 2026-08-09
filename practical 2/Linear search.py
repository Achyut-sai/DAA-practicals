import time


def linear_search(arr, target):
    """Performs Linear Search on a list.

    Time Complexities:
      - Best Case: O(1)    -> Target is at the first index.
      - Average Case: O(n) -> Target is around the middle.
      - Worst Case: O(n)   -> Target is at the last index or not present.

    Space Complexity: O(1)
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1


# 1. User Input
try:
    user_input = input("Enter space-separated numbers: ")
    arr = [int(x) for x in user_input.split()]
    target = int(input("Enter target number to search: "))

    # 2. Measure Execution Time
    start_time = time.perf_counter()
    result = linear_search(arr, target)
    end_time = time.perf_counter()

    # 3. Display Results
    execution_time_ms = (end_time - start_time) * 1000

    if result != -1:
        print(f"\n[Result]: Target {target} found at index {result}.")
    else:
        print(f"\n[Result]: Target {target} not found in the array.")

    print(f"Execution Time: {execution_time_ms:.6f} ms")

except ValueError:
    print("Invalid input! Please enter valid integers.")
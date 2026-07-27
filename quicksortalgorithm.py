import time


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Driver Code with User Input & Benchmarking
if __name__ == "__main__":
    user_input = input(
        "Quick Sort - Enter integers separated by space: "
    ).strip()
    arr = [int(x) for x in user_input.split()]

    start_time = time.perf_counter_ns()
    sorted_arr = quick_sort(arr)
    end_time = time.perf_counter_ns()

    exec_time_ms = (end_time - start_time) / 1_000_000

    print("\n--- RESULTS ---")
    print(f"Sorted Output   : {sorted_arr}")
    print(f"Execution Time  : {exec_time_ms:.5f} ms")
    print(f"Best Complexity : O(n log n)")
    print(f"Avg Complexity  : O(n log n)")
    print(f"Worst Complexity: O(n²)")
    print(f"Space Complexity: O(log n)")
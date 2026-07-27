import time


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Driver Code with User Input & Benchmarking
if __name__ == "__main__":
    user_input = input(
        "Selection Sort - Enter integers separated by space: "
    ).strip()
    arr = [int(x) for x in user_input.split()]

    start_time = time.perf_counter_ns()
    sorted_arr = selection_sort(arr)
    end_time = time.perf_counter_ns()

    exec_time_ms = (end_time - start_time) / 1_000_000

    print("\n--- RESULTS ---")
    print(f"Sorted Output   : {sorted_arr}")
    print(f"Execution Time  : {exec_time_ms:.5f} ms")
    print(f"Best Complexity : O(n²)")
    print(f"Avg Complexity  : O(n²)")
    print(f"Worst Complexity: O(n²)")
    print(f"Space Complexity: O(1)")
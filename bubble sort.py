import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Driver Code with User Input & Benchmarking
if __name__ == "__main__":
    user_input = input(
        "Bubble Sort - Enter integers separated by space: "
    ).strip()
    arr = [int(x) for x in user_input.split()]

    start_time = time.perf_counter_ns()
    sorted_arr = bubble_sort(arr)
    end_time = time.perf_counter_ns()

    exec_time_ms = (end_time - start_time) / 1_000_000

    print("\n--- RESULTS ---")
    print(f"Sorted Output   : {sorted_arr}")
    print(f"Execution Time  : {exec_time_ms:.5f} ms")
    print(f"Best Complexity : O(n)")
    print(f"Avg Complexity  : O(n²)")
    print(f"Worst Complexity: O(n²)")
    print(f"Space Complexity: O(1)")
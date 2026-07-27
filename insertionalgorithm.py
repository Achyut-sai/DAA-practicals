import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Driver Code with User Input & Benchmarking
if __name__ == "__main__":
    user_input = input(
        "Insertion Sort - Enter integers separated by space: "
    ).strip()
    arr = [int(x) for x in user_input.split()]

    start_time = time.perf_counter_ns()
    sorted_arr = insertion_sort(arr)
    end_time = time.perf_counter_ns()

    exec_time_ms = (end_time - start_time) / 1_000_000

    print("\n--- RESULTS ---")
    print(f"Sorted Output   : {sorted_arr}")
    print(f"Execution Time  : {exec_time_ms:.5f} ms")
    print(f"Best Complexity : O(n)")
    print(f"Avg Complexity  : O(n²)")
    print(f"Worst Complexity: O(n²)")
    print(f"Space Complexity: O(1)")
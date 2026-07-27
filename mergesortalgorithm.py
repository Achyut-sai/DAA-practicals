import time


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Driver Code with User Input & Benchmarking
if __name__ == "__main__":
    user_input = input(
        "Merge Sort - Enter integers separated by space: "
    ).strip()
    arr = [int(x) for x in user_input.split()]

    start_time = time.perf_counter_ns()
    sorted_arr = merge_sort(arr)
    end_time = time.perf_counter_ns()

    exec_time_ms = (end_time - start_time) / 1_000_000

    print("\n--- RESULTS ---")
    print(f"Sorted Output   : {sorted_arr}")
    print(f"Execution Time  : {exec_time_ms:.5f} ms")
    print(f"Best Complexity : O(n log n)")
    print(f"Avg Complexity  : O(n log n)")
    print(f"Worst Complexity: O(n log n)")
    print(f"Space Complexity: O(n)")
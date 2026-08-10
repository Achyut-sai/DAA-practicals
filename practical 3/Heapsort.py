import time


# ---------------------------------------------------------
# MAX HEAPIFY
# ---------------------------------------------------------
def max_heapify(arr, n, i):
    largest = i          # Assume root is largest
    left = 2 * i + 1     # Left child
    right = 2 * i + 2     # Right child

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected subtree
        max_heapify(arr, n, largest)


# ---------------------------------------------------------
# BUILD MAX HEAP
# ---------------------------------------------------------
def build_max_heap(arr):
    n = len(arr)

    # Start from the last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


# ---------------------------------------------------------
# HEAP SORT
# ---------------------------------------------------------
def heap_sort(arr):
    n = len(arr)

    # Step 1: Build Max Heap
    build_max_heap(arr)

    print("\nMax Heap:")
    print(arr)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):

        # Move maximum element to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Restore Max Heap property
        max_heapify(arr, i, 0)


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------
print("========== MAX HEAP SORT ==========")

# User input
n = int(input("Enter number of elements: "))

arr = []

print("Enter", n, "elements:")

for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    arr.append(value)

print("\nOriginal Array:")
print(arr)

# Measure execution time
start_time = time.perf_counter()

heap_sort(arr)

end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

print("\nSorted Array:")
print(arr)

print("\nExecution Time:")
print(f"{execution_time:.10f} seconds")

print("\n========== TIME COMPLEXITY ==========")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n log n)")

print("\nSpace Complexity: O(log n) due to recursive max_heapify()")
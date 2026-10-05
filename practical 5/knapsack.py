def knapsack_dp(weights, values, capacity):
    n = len(weights)
    operations = 0  # counts DP cell computations

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            operations += 1
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]
    selected.reverse()

    return dp[n][capacity], selected, dp, operations


def print_dp_table(dp, n, capacity):
    print("\nDP Table (rows = items, columns = capacity):")
    print("     " + " ".join(f"{w:3d}" for w in range(capacity + 1)))
    print("     " + "----" * (capacity + 1))
    for i in range(n + 1):
        print(f"i={i:2d}|" + " ".join(f"{dp[i][w]:3d}" for w in range(capacity + 1)))


def get_int(prompt, allow_zero=False):
    while True:
        try:
            value = int(input(prompt))
            if value < 0 or (value == 0 and not allow_zero):
                print("Please enter a valid positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    print("=" * 55)
    print("   0/1 KNAPSACK PROBLEM USING DYNAMIC PROGRAMMING")
    print("=" * 55)

    n = get_int("Enter number of items: ")

    weights, values = [], []
    for i in range(n):
        print(f"\nItem {i + 1}:")
        weights.append(get_int("  Weight : "))
        values.append(get_int("  Value  : ", allow_zero=True))

    capacity = get_int("\nEnter knapsack capacity: ")

    max_value, selected, dp, operations = knapsack_dp(weights, values, capacity)

    print("\n" + "=" * 55)
    print("RESULT")
    print("=" * 55)
    print(f"Maximum value achievable  : {max_value}")
    print(f"Selected items (1-indexed): {[i + 1 for i in selected]}")
    print(f"Total weight of selection : {sum(weights[i] for i in selected)} / {capacity}")

    print("\nItem Details:")
    print(f"{'Item':<6}{'Weight':<10}{'Value':<10}")
    for i in selected:
        print(f"{i + 1:<6}{weights[i]:<10}{values[i]:<10}")

    if n <= 10 and capacity <= 20:
        print_dp_table(dp, n, capacity)

    print("\n" + "=" * 55)
    print("EXECUTION ANALYSIS")
    print("=" * 55)
    print(f"DP cells computed (operations) : {operations}")
    print(f"Expected n * W                 : {n} * {capacity} = {n * capacity}")

    print("\nTIME & SPACE COMPLEXITY")
    print("-" * 55)
    print(f"Time Complexity  : O(n * W) = O({n * capacity})")
    print(f"Space Complexity : O(n * W) = O({n * capacity})")
    print("  (can be reduced to O(W) with a 1-D array)")
    print("-" * 55)


main()
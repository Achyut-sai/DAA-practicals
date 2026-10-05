Summary

This practical implements the 0/1 Knapsack Problem using Dynamic Programming. Given n items, each with a weight and a value, and a knapsack of capacity W, the goal is to choose items so that the total value is maximum without the total weight exceeding W. Each item can be taken whole or not at all (0/1 property).


Conclusion

The 0/1 Knapsack problem was successfully implemented using dynamic programming. By storing solutions to overlapping subproblems in a table, the program avoids the repeated computation of the brute-force approach and reduces the time from exponential O(2ⁿ) to pseudo-polynomial O(n × W). The operation count matched n × W exactly, which verified the theoretical time complexity. The method also gives the optimal solution, not just an approximation, and can be made more memory-efficient with a 1-D array when only the maximum value is needed. Its limitation is that running time grows with the capacity W, so it becomes slow for very large capacities. Overall, the practical shows how dynamic programming is an effective technique for optimisation problems with optimal substructure and overlapping subproblems.
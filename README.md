# Route Optimizer using TSP

## Coding Skills Project Submission

This project implements a route optimization system based on the Travelling Salesman Problem (TSP). It determines the shortest possible path that visits all given cities exactly once and returns to the starting point.

---

## Algorithms Used

* Brute Force (Exact Solution)
* Greedy Algorithm (Nearest Neighbor Heuristic)

---

## Features

* Manual input of city coordinates
* Random city generation for testing
* Distance calculation using Euclidean formula
* Computes optimal route and total cost
* Compares execution time of different algorithms
* User-friendly console interaction

---

## How to Run

```bash
python main.py
```

## Sample Output

```
==============================
   ROUTE OPTIMIZER (TSP)
==============================

Cities:
0 -> (0, 0)
1 -> (7, 5)
2 -> (6, 7)
3 -> (10, 8)

Brute Force Solution:
Route: 0 -> 1 -> 3 -> 2 -> 0
Cost : 26.19
Time : 0.000082 sec

Greedy Solution:
Route: 0 -> 1 -> 2 -> 3 -> 0
Cost : 27.77
Time : 0.000112 sec

## Technologies Used

* Python
* Standard Libraries: itertools, math, random, time

---

## Conclusion

This project demonstrates the application of algorithmic techniques to solve optimization problems, highlighting the difference between exact and heuristic approaches in terms of accuracy and performance.

import itertools
import math
import random
import time

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = calculate_distance(cities[i], cities[j])
    return dist

def tsp_brute_force(dist):
    n = len(dist)
    cities = list(range(n))
    min_cost = float('inf')
    best_path = []

    for perm in itertools.permutations(cities[1:]):
        path = [0] + list(perm) + [0]
        cost = sum(dist[path[i]][path[i+1]] for i in range(n))
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

def tsp_greedy(dist):
    n = len(dist)
    visited = [False]*n
    path = [0]
    visited[0] = True
    cost = 0

    for _ in range(n-1):
        last = path[-1]
        next_city = None
        min_dist = float('inf')

        for i in range(n):
            if not visited[i] and dist[last][i] < min_dist:
                min_dist = dist[last][i]
                next_city = i

        path.append(next_city)
        visited[next_city] = True
        cost += min_dist

    cost += dist[path[-1]][0]
    path.append(0)

    return path, cost

def generate_random_cities(n):
    return [(random.randint(0, 10), random.randint(0, 10)) for _ in range(n)]

def get_user_cities():
    n = int(input("Enter number of cities: "))
    cities = []

    print("Enter coordinates (x y):")
    for i in range(n):
        x, y = map(int, input(f"City {i}: ").split())
        cities.append((x, y))

    return cities

def main():
    while True:
        print("   ROUTE OPTIMIZER (TSP)")
        print("1. Enter cities manually")
        print("2. Generate random cities")

        choice = int(input("\nEnter choice: "))

        if choice == 1:
            cities = get_user_cities()
        elif choice == 2:
            n = int(input("Enter number of cities (<=8 recommended): "))
            cities = generate_random_cities(n)
        else:
            print("Invalid choice!")
            continue

        print("\nCities:")
        for i, city in enumerate(cities):
            print(f"{i} -> {city}")

        dist = create_distance_matrix(cities)

        # Brute Force
        start = time.time()
        bf_path, bf_cost = tsp_brute_force(dist)
        bf_time = time.time() - start

        # Greedy
        start = time.time()
        gr_path, gr_cost = tsp_greedy(dist)
        gr_time = time.time() - start

      
        print("\nBrute Force Solution:")
        print("Route:", " -> ".join(map(str, bf_path)))
        print("Cost :", round(bf_cost, 2))
        print("Time :", round(bf_time, 6), "sec")

        print("\nGreedy Solution:")
        print("Route:", " -> ".join(map(str, gr_path)))
        print("Cost :", round(gr_cost, 2))
        print("Time :", round(gr_time, 6), "sec")

        print("\n1. Run again")
        print("2. Exit")

        again = int(input("Enter choice: "))

        if again == 2:
            print("Exiting program...")
            break
if __name__ == "__main__":
    main()
import random
import time
import math
from typing import List, Tuple
def clustered_points(n, clusters=3, spread=20):
    centers = [(random.random() * 1000, random.random() * 1000) for
    _ in range(clusters)]
    pts = []
    for cx, cy in centers:
        for _ in range(n // clusters):
            x = random.gauss(cx, spread)
            y = random.gauss(cy, spread)
            pts.append((x, y))
    return pts


pts = clustered_points(50)

# Taken from optimal_closest_pair.py
Point = Tuple[float, float]

def sqdist(a: Point, b: Point) -> float:
    """Return squared Euclidean distance between two points."""
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy

# Brute force method for small inputs

def brute_force(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    """Compute smallest squared distance by brute force."""
    best = float("inf")
    pair = (points[0], points[1])
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = sqdist(points[i], points[j])
            if d < best:
                best = d
                pair = (points[i], points[j])
    return best, pair

# Divide and Conquer method

def closest_rec(Px: List[Point], Py: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    n = len(Px)
    if n <= 3:
        return brute_force(Px)

    mid = n // 2
    Qx = Px[:mid]
    Rx = Px[mid:]
    midx = Px[mid][0]

    # Partition Py into Qy and Ry
    Qy, Ry = [], []
    for p in Py:
        if p[0] <= midx:
            Qy.append(p)
        else:
            Ry.append(p)

    dl, pairl = closest_rec(Qx, Qy)
    dr, pairr = closest_rec(Rx, Ry)

    # Choose smaller of two sides
    if dl <= dr:
        d = dl
        best_pair = pairl
    else:
        d = dr
        best_pair = pairr

    # Build strip (points within sqrt(d) of mid line)

    strip = [p for p in Py if (p[0] - midx) ** 2 < d]

    # Check strip points (compare up to 7 next points)

    m = len(strip)
    for i in range(m):
        j = i + 1
        while j < m and (strip[j][1] - strip[i][1]) ** 2 < d:
            dst = sqdist(strip[i], strip[j])
            if dst < d:
                d = dst
                best_pair = (strip[i], strip[j])
            j += 1

    return d, best_pair


# Main function to call

def closest_pair(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    """Return actual closest distance and the pair of points."""
    if len(points) < 2:
        raise ValueError("Need at least two points")

    Px = sorted(points, key=lambda p: (p[0], p[1]))
    Py = sorted(points, key=lambda p: (p[1], p[0]))
    d_sq, pair = closest_rec(Px, Py)
    return math.sqrt(d_sq), pair  # convert to actual distance here


# Compare Divide & Conquer vs Brute Force
start =  time.perf_counter()
d, pair = closest_pair(pts)
end = time.perf_counter()
print("Closest distance (Divide and Conquer):", d)
print("Closest pair (Divide and Conquer):", pair)
print("Time taken",{end-start},"seconds")
start = time.perf_counter()
d_bf, pair_bf = brute_force(pts)
d_bf = math.sqrt(d_bf)
# convert to real distance for comparison
end = time.perf_counter()
print("Closest distance (Brute Force):", d_bf)
print("Closest pair (Brute Force):", pair_bf)
print("Time taken", {end-start},"seconds")

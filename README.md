# Closest-Pair of Points

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3%2B-brightgreen.svg)](https://www.python.org/downloads/)

A Python implementation of the **Closest Pair of Points** problem in computational geometry — finding the two points that are the minimum distance apart from a given set of points in the plane.  
This repository includes both a **brute-force** approach and an **optimized divide-and-conquer** algorithm.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Algorithms Implemented](#algorithms-implemented)
- [External Libraries](#external-libraries)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Performance / Complexity](#performance--complexity)
- [Testing & Examples](#testing--examples)
- [Acknowledgements](#acknowledgements)

---

## About

The *Closest Pair of Points* problem asks:  
> Given n points in a 2D plane, find the pair with the smallest Euclidean distance.

It’s a fundamental **computational geometry** problem with real-world applications in:  
- Spatial data analysis  
- Geographic Information Systems (GIS)

This repository includes:
- A **Brute Force** approach **O(n²)**
- A **Divide & Conquer** approach **O(n log n)**

---

## Features

- Clean, easy-to-read Python code  
- Comparison between brute-force and optimized methods  
- Uses standard and widely supported Python libraries  

---

## External Libraries

The following Python libraries are used:

| Library | Purpose |
|----------|----------|
| `typing` | Type hinting for cleaner, safer code |
| `math` | For Euclidean distance calculations |
| `time` | Runtime performance comparison |
| `random` | Random point generation for testing |
| `pandas` | Data handling, result tabulation, and optional export |


---

## Algorithms Implemented

### 1 Clustered Points (`clustered_points.py`)
- Checks all \(\binom{n}{2}\) point pairs.  
- Time complexity: **O(n²)**.  
- Best suited for small datasets.

### 2 Optimal Closest Pair (`optimal_closest_pair.py`)
- Splits points by x-coordinate, recursively finds closest pairs, and merges results efficiently.  
- Time complexity: **O(n log n)**.  
- Ideal for large datasets.

---

##  Getting Started

### 🔧 Prerequisites
- Python 3.14  
- `pip` (Python package installer)

### Installation

Clone the repository:
```bash
git clone https://github.com/arkapriyo/Closest-Pair-of-Points.git
cd Closest-Pair-of-Points
```

---

## Usage

Run either implementation directly:

```bash
# Clustered Distribution
python clustered_points.py

# Optimal Implementation
python optimal_closest_pair.py
```

---

## Performance / Complexity

| Algorithm | Time Complexity | Space Complexity | Suitable For |
|------------|----------------|------------------|---------------|
| Brute Force | O(n²) | O(1) | Small datasets |
| Divide-and-Conquer | O(n log n) | O(n) | Large datasets |

Both methods return the same result but differ in runtime efficiency.

---

## Testing & Examples

You can easily modify the points for testing:

```python
points = [(0, 0), (1, 1), (2, 2), (3, 3)]
```

Expected output:
```
Closest pair: ((0, 0), (1, 1))
Distance: 1.4142
```

You can also generate random points using:
```python
import random
points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(100)]
```

---

## Authors
- [Arkapriyo Hore](https://github.com/arkapriyo) (BMAT2313)
- Bodhideep Joardar (BMAT2315)

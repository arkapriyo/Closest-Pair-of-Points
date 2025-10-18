# Closest-Pair of Points

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3%2B-brightgreen.svg)](https://www.python.org/downloads/)

A Python implementation of the **Closest Pair of Points** problem in computational geometry — finding the two points that are the minimum distance apart from a given set of points in the plane.  
This repository includes both a **brute-force** approach and an **optimized divide-and-conquer** algorithm.

---

## 📖 Table of Contents

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
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## 🧩 About

The *Closest Pair of Points* problem asks:  
> Given \(n\) points in a 2D plane, find the pair with the smallest Euclidean distance.

It’s a fundamental **computational geometry** problem with real-world applications in:
- Computer graphics  
- Clustering and machine learning  
- Spatial data analysis  
- Geographic Information Systems (GIS)

This repository includes:
- A **Brute Force** approach (\(O(n^2)\))
- A **Divide & Conquer** approach (\(O(n \log n)\))

---

## ✨ Features

- Clean, easy-to-read Python code  
- Comparison between brute-force and optimized methods  
- Uses standard and widely supported Python libraries  
- Educational structure — great for learning divide and conquer  

---

## 🧱 External Libraries

The following Python libraries are used:

| Library | Purpose |
|----------|----------|
| `typing` | Type hinting for cleaner, safer code |
| `math` | For Euclidean distance calculations |
| `time` | Runtime performance comparison |
| `random` | Random point generation for testing |
| `pandas` | Data handling, result tabulation, and optional export |

Install them with:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Algorithms Implemented

### 1️⃣ Brute Force (`clustered_points.py`)
- Checks all \(\binom{n}{2}\) point pairs.  
- Time complexity: **O(n²)**.  
- Best suited for small datasets.

### 2️⃣ Divide-and-Conquer (`optimal_closest_pair.py`)
- Splits points by x-coordinate, recursively finds closest pairs, and merges results efficiently.  
- Time complexity: **O(n log n)**.  
- Ideal for large datasets.

---

## 🚀 Getting Started

### 🔧 Prerequisites
- Python 3.7 or above  
- `pip` (Python package installer)

### 💻 Installation

Clone the repository:
```bash
git clone https://github.com/arkapriyo/Closest-Pair-of-Points.git
cd Closest-Pair-of-Points
```

Install required packages:
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run either implementation directly:

```bash
# Brute-force version
python clustered_points.py

# Divide and conquer version
python optimal_closest_pair.py
```

Or use the functions in your own code:

```python
from optimal_closest_pair import closest_pair

points = [(1.0, 2.0), (3.5, 4.2), (-0.5, 0.1)]
(pair, distance) = closest_pair(points)
print(f"Closest points: {pair} with distance = {distance:.4f}")
```

---

## ⏱️ Performance / Complexity

| Algorithm | Time Complexity | Space Complexity | Suitable For |
|------------|----------------|------------------|---------------|
| Brute Force | O(n²) | O(1) | Small datasets |
| Divide-and-Conquer | O(n log n) | O(n) | Large datasets |

Both methods return the same result but differ in runtime efficiency.

---

## 🧪 Testing & Examples

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

## 🤝 Contributing

Contributions are welcome! 🎉  
Suggestions and pull requests that improve readability, efficiency, or add features are highly appreciated.

To contribute:
1. Fork the repo  
2. Create a new branch (`feature-branch`)  
3. Commit your changes  
4. Submit a pull request  

Please ensure:
- Code follows **PEP8** style guidelines  
- Include docstrings and comments for clarity  

---

## 📜 License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## 🙌 Authors
- [Arkapriyo Hore](https://github.com/arkapriyo) (BMAT2313)
- Bodhideep Joardar (BMAT2315)

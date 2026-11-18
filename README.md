# Numerical Methods: Differentiation and Integration

A collection of Python implementations of numerical methods studied in numerical analysis. This repository is part of my ongoing practice in understanding numerical algorithms and translating their mathematical formulas into code.

## Methods Included

### Ordinary Differential Equations (ODEs)

The following methods are implemented for approximating solutions to initial-value problems:

| File | Method |
|---|---|
| `01_euler.py` | Euler's Method |
| `02_modified_euler.py` | Modified Euler's Method |
| `03_heun.py` | Heun's Method |
| `04_midpoint.py` | Midpoint Method |
| `05_ralston.py` | Ralston's Method |
| `06_rk4.py` | Fourth-Order Runge–Kutta (RK4) |

### Numerical Integration

The following methods are implemented to approximate definite integrals:

| File | Method |
|---|---|
| `07_trapezoidal.py` | Trapezoidal Rule |
| `08_simpson_1_3.py` | Simpson's 1/3 Rule |
| `09_simpson_3_8.py` | Simpson's 3/8 Rule |
| `10_weddle.py` | Weddle's Rule |

## Project Structure

```text
.
├── README.md
└── NM_D_I/
    ├── 01_euler.py
    ├── 02_modified_euler.py
    ├── 03_heun.py
    ├── 04_midpoint.py
    ├── 05_ralston.py
    ├── 06_rk4.py
    ├── 07_trapezoidal.py
    ├── 08_simpson_1_3.py
    ├── 09_simpson_3_8.py
    └── 10_weddle.py
```

## Requirements

- Python 3
- No third-party packages are required by the current scripts.

## How to Run

Clone the repository:

```bash
git clone https://github.com/Taherislam219/Numerical-Methods-Differentiation-and-Integration.git
cd Numerical-Methods-Differentiation-and-Integration
```

Run an individual method from the project root. For example:

```bash
python NM_D_I/06_rk4.py
python NM_D_I/08_simpson_1_3.py
```

Each script currently contains its own example function and numerical parameters. Open the relevant Python file to adjust the function, initial values, interval, or step size.

## Learning Purpose

This repository is intended for academic practice and learning. It helps me explore how different numerical methods work and compare their approaches to approximating solutions and integrals.

More methods and improvements may be added as I continue learning.

---

**Status:** Learning project — actively evolving.

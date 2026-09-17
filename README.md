# AdvanceMath_cp 🧮

A curated collection of essential **Number Theory & Advanced Mathematics** algorithms implemented in Python for Competitive Programming (CP) and algorithmic problem-solving.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Summary & Complexity Matrix](#summary--complexity-matrix)
- [Algorithms & File Documentation](#algorithms--file-documentation)
  - [1. Euclidean Algorithm (`EuclideanAlgo.py`)](#1-euclidean-algorithm-euclideanalgopy)
  - [2. Extended Euclidean Algorithm (`ExtendedEuclideanAlgo.py`)](#2-extended-euclidean-algorithm-extendedeuclideanalgopy)
  - [3. Linear Diophantine Equations (`LinearDiophantineEquations.py`)](#3-linear-diophantine-equations-lineardiophantineequationspy)
  - [4. Modular Multiplicative Inverse (`Mod_Inverse.py`)](#4-modular-multiplicative-inverse-mod_inversepy)
  - [5. Fermat's Little Theorem (`FermatLittleTheorem.py`)](#5-fermats-little-theorem-fermatlittletheorempy)
  - [6. Primality Test (`Is_prime.py`)](#6-primality-test-is_primepy)
  - [7. Prime Factorization (`PrimeFactorization.py`)](#7-prime-factorization-primefactorizationpy)
  - [8. Sieve of Eratosthenes (`SeiveofEratosthenes.py`)](#8-sieve-of-eratosthenes-seiveoferatosthenespy)
  - [9. Smallest Prime Factor Sieve (`SmallestPrimeFactorSieve.py`)](#9-smallest-prime-factor-sieve-smallestprimefactorsievepy)
  - [10. Euler's Totient for Single Number (`EulerTotientforOnenumber.py`)](#10-eulers-totient-for-single-number-eulertotientforonenumberpy)
  - [11. Euler's Totient Sieve (`TotientSieve.py`)](#11-eulers-totient-sieve-totientsievepy)
- [How to Run](#how-to-run)

---

## 🚀 Overview

Number theory is foundational in competitive programming platforms such as Codeforces, AtCoder, LeetCode, and CodeChef. This repository contains optimized, clean, and tested Python implementations of fundamental mathematical algorithms covering:
- Greatest Common Divisors & Bézout's Identity
- Linear Diophantine Equations
- Modular Inverses & Modular Arithmetic
- Prime Generation, Testing, and Factorization
- Euler's Totient Functions (Single & Sieve)

---

## 📊 Summary & Complexity Matrix

| File | Algorithm | Time Complexity | Space Complexity | Primary Use Case |
| :--- | :--- | :--- | :--- | :--- |
| [`EuclideanAlgo.py`](./EuclideanAlgo.py) | Euclidean Algorithm | $O(\log(\min(a, b)))$ | $O(1)$ | Find $\gcd(a, b)$ |
| [`ExtendedEuclideanAlgo.py`](./ExtendedEuclideanAlgo.py) | Extended Euclidean Algorithm | $O(\log(\min(a, b)))$ | $O(\log(\min(a, b)))$ | Find $\gcd$ and Bézout coefficients $(x, y)$ |
| [`LinearDiophantineEquations.py`](./LinearDiophantineEquations.py) | Diophantine Solvability | $O(\log(\min(a, b)))$ | $O(1)$ | Check existence of integer solution for $ax + by = c$ |
| [`Mod_Inverse.py`](./Mod_Inverse.py) | General Modular Inverse | $O(\log(\min(a, m)))$ | $O(\log(\min(a, m)))$ | Find $a^{-1} \pmod m$ when $\gcd(a, m) = 1$ |
| [`FermatLittleTheorem.py`](./FermatLittleTheorem.py) | Modular Inverse (Prime Modulo) | $O(\log p)$ | $O(1)$ | Fast $a^{-1} \pmod p$ when $p$ is prime |
| [`Is_prime.py`](./Is_prime.py) | Trial Division Primality Test | $O(\sqrt{n})$ | $O(1)$ | Single-query primality checking |
| [`PrimeFactorization.py`](./PrimeFactorization.py) | Trial Division Factorization | $O(\sqrt{n})$ | $O(\log n)$ | Single-query prime factor decomposition |
| [`SeiveofEratosthenes.py`](./SeiveofEratosthenes.py) | Sieve of Eratosthenes | $O(n \log(\log n))$ | $O(n)$ | Fast prime generation up to $n$ |
| [`SmallestPrimeFactorSieve.py`](./SmallestPrimeFactorSieve.py) | SPF Sieve | $O(M \log(\log M))$ prep, $O(1)$ query | $O(M)$ | Fast $O(\log n)$ multiple-query factorization |
| [`EulerTotientforOnenumber.py`](./EulerTotientforOnenumber.py) | Euler's Phi (Single) | $O(\sqrt{n})$ | $O(1)$ | Count coprimes $\le n$ for a single number |
| [`TotientSieve.py`](./TotientSieve.py) | Euler's Phi Sieve | $O(n \log(\log n))$ | $O(n)$ | Precompute $\phi(1 \dots n)$ for all values up to $10^6$ |

---

## 📖 Algorithms & File Documentation

### 1. Euclidean Algorithm (`EuclideanAlgo.py`)
- **File**: [`EuclideanAlgo.py`](./EuclideanAlgo.py)
- **Description**: Efficiently computes the Greatest Common Divisor (GCD) of two non-negative integers $a$ and $b$ using the division remainder step repeatedly until the remainder becomes zero.
- **Mathematical Formula**:
  $$\gcd(a, b) = \begin{cases} a & \text{if } b = 0 \\ \gcd(b, a \bmod b) & \text{if } b > 0 \end{cases}$$
- **Time Complexity**: $\mathcal{O}(\log(\min(a, b)))$
- **Space Complexity**: $\mathcal{O}(1)$ (Iterative)
- **Example**:
  ```python
  # Input: 48 18
  # Output: 6
  ```

---

### 2. Extended Euclidean Algorithm (`ExtendedEuclideanAlgo.py`)
- **File**: [`ExtendedEuclideanAlgo.py`](./ExtendedEuclideanAlgo.py)
- **Description**: In addition to computing $g = \gcd(a, b)$, it computes integer coefficients $x$ and $y$ that satisfy **Bézout's Identity**.
- **Mathematical Formula**:
  $$a \cdot x + b \cdot y = \gcd(a, b)$$
  Using the recursive step where $\gcd(b, a \bmod b) = b \cdot x_1 + (a \bmod b) \cdot y_1$:
  $$\because a \bmod b = a - \left\lfloor \frac{a}{b} \right\rfloor \cdot b$$
  $$a \cdot y_1 + b \cdot \left(x_1 - \left\lfloor \frac{a}{b} \right\rfloor \cdot y_1\right) = \gcd(a, b)$$
  $$\implies x = y_1, \quad y = x_1 - \left\lfloor \frac{a}{b} \right\rfloor \cdot y_1$$
  - Base case: When $b = 0$, $\gcd(a, 0) = a$, with $x = 1, y = 0$ since $a(1) + 0(0) = a$.
- **Time Complexity**: $\mathcal{O}(\log(\min(a, b)))$
- **Space Complexity**: $\mathcal{O}(\log(\min(a, b)))$ (Recursive stack)

---

### 3. Linear Diophantine Equations (`LinearDiophantineEquations.py`)
- **File**: [`LinearDiophantineEquations.py`](./LinearDiophantineEquations.py)
- **Description**: Determines whether an integer solution $(x, y) \in \mathbb{Z}^2$ exists for a linear Diophantine equation of the form $ax + by = c$.
- **Mathematical Formula & Theorem**:
  A linear Diophantine equation $ax + by = c$ has integer solutions if and only if the greatest common divisor of $a$ and $b$ divides $c$:
  $$c \bmod \gcd(a, b) = 0 \iff \gcd(a, b) \mid c$$
  If a particular solution $(x_0, y_0)$ exists (obtained via Extended Euclidean Algorithm), the general set of all solutions for any integer $k \in \mathbb{Z}$ is:
  $$x = x_0 \cdot \frac{c}{g} + k \cdot \frac{b}{g}, \quad y = y_0 \cdot \frac{c}{g} - k \cdot \frac{a}{g} \quad \text{where } g = \gcd(a, b)$$
- **Time Complexity**: $\mathcal{O}(\log(\min(a, b)))$
- **Space Complexity**: $\mathcal{O}(1)$

---

### 4. Modular Multiplicative Inverse (`Mod_Inverse.py`)
- **File**: [`Mod_Inverse.py`](./Mod_Inverse.py)
- **Description**: Computes the modular multiplicative inverse $x = a^{-1} \pmod m$ such that $a \cdot x \equiv 1 \pmod m$ for arbitrary modulus $m$ using the Extended Euclidean Algorithm.
- **Mathematical Formula**:
  $$a \cdot x \equiv 1 \pmod m \iff a \cdot x + m \cdot y = 1$$
  - An inverse exists **if and only if** $\gcd(a, m) = 1$ (i.e., $a$ and $m$ are coprime).
  - The positive canonical inverse is given by:
    $$x = (x \bmod m + m) \bmod m$$
- **Time Complexity**: $\mathcal{O}(\log(\min(a, m)))$
- **Space Complexity**: $\mathcal{O}(\log(\min(a, m)))$

---

### 5. Fermat's Little Theorem (`FermatLittleTheorem.py`)
- **File**: [`FermatLittleTheorem.py`](./FermatLittleTheorem.py)
- **Description**: Computes modular inverse extremely quickly when the modulus $p$ is a **prime number** and $\gcd(a, p) = 1$.
- **Mathematical Formula & Theorem**:
  Fermat's Little Theorem states that if $p$ is a prime number and $\gcd(a, p) = 1$:
  $$a^{p-1} \equiv 1 \pmod p$$
  Multiplying both sides by $a^{-1}$:
  $$a \cdot a^{p-2} \equiv 1 \pmod p \implies a^{-1} \equiv a^{p-2} \pmod p$$
  Implemented using Python's fast modular exponentiation `pow(a, p - 2, p)`.
- **Time Complexity**: $\mathcal{O}(\log p)$
- **Space Complexity**: $\mathcal{O}(1)$

---

### 6. Primality Test (`Is_prime.py`)
- **File**: [`Is_prime.py`](./Is_prime.py)
- **Description**: Checks whether a given integer $n$ is prime using optimized trial division up to $\sqrt{n}$.
- **Mathematical Formula**:
  Any composite number $n$ must possess at least one non-trivial factor $d$ such that $2 \le d \le \lfloor\sqrt{n}\rfloor$.
  If no integer $i \in [2, \lfloor\sqrt{n}\rfloor]$ evenly divides $n$, then $n$ is prime for $n \ge 2$.
- **Time Complexity**: $\mathcal{O}(\sqrt{n})$ per test case
- **Space Complexity**: $\mathcal{O}(1)$

---

### 7. Prime Factorization (`PrimeFactorization.py`)
- **File**: [`PrimeFactorization.py`](./PrimeFactorization.py)
- **Description**: Decomposes a given integer $n$ into its canonical prime factorization product.
- **Mathematical Formula**:
  By the **Fundamental Theorem of Arithmetic**:
  $$n = p_1^{a_1} \cdot p_2^{a_2} \cdots p_k^{a_k}$$
  where each $p_i$ is a distinct prime and $a_i \ge 1$.
  The algorithm repeatedly removes each factor $p$ while testing $p \le \sqrt{n}$. Any remaining $n > 1$ after loop termination is itself prime.
- **Time Complexity**: $\mathcal{O}(\sqrt{n})$
- **Space Complexity**: $\mathcal{O}(\log n)$ (to store prime factors)

---

### 8. Sieve of Eratosthenes (`SeiveofEratosthenes.py`)
- **File**: [`SeiveofEratosthenes.py`](./SeiveofEratosthenes.py)
- **Description**: Highly optimized algorithm to find and generate all prime numbers up to a given limit $n$.
- **Mathematical Formula**:
  Maintains a boolean array `prime[0...n]`. Starting from $p = 2$, whenever `prime[p]` is true, marks all composite multiples starting from $p^2$ in steps of $p$:
  $$\text{Mark false for } i \in \{p^2, p^2 + p, p^2 + 2p, \dots \le n\}$$
- **Time Complexity**: $\mathcal{O}(n \log(\log n))$
- **Space Complexity**: $\mathcal{O}(n)$

---

### 9. Smallest Prime Factor Sieve (`SmallestPrimeFactorSieve.py`)
- **File**: [`SmallestPrimeFactorSieve.py`](./SmallestPrimeFactorSieve.py)
- **Description**: Precomputes the Smallest Prime Factor (SPF) for every integer up to a maximum value $M$. Enables full prime factorization in $\mathcal{O}(\log n)$ time per query.
- **Mathematical Formula**:
  $$\text{spf}[i] = \min \{ p \mid p \text{ is prime and } p \text{ divides } i \}$$
  For each prime $p$, assign $\text{spf}[k \cdot p] = p$ for all previously unmarked multiples $k \cdot p \ge p^2$.
- **Time Complexity**:
  - **Precomputation**: $\mathcal{O}(M \log(\log M))$
  - **Query (Factorization / SPF lookup)**: $\mathcal{O}(1)$ lookup, $\mathcal{O}(\log n)$ full factorization
- **Space Complexity**: $\mathcal{O}(M)$

---

### 10. Euler's Totient for Single Number (`EulerTotientforOnenumber.py`)
- **File**: [`EulerTotientforOnenumber.py`](./EulerTotientforOnenumber.py)
- **Description**: Computes Euler's Totient function $\phi(n)$, which counts the number of integers $k \in [1, n]$ that are coprime to $n$ ($\gcd(k, n) = 1$).
- **Mathematical Formula**:
  **Euler's Product Formula**:
  $$\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right) = n \prod_{p \mid n} \frac{p - 1}{p}$$
  where the product is over all distinct prime factors $p$ dividing $n$.
  In integer arithmetic:
  $$\text{res} \leftarrow \text{res} - \left\lfloor \frac{\text{res}}{p} \right\rfloor$$
- **Time Complexity**: $\mathcal{O}(\sqrt{n})$
- **Space Complexity**: $\mathcal{O}(1)$

---

### 11. Euler's Totient Sieve (`TotientSieve.py`)
- **File**: [`TotientSieve.py`](./TotientSieve.py)
- **Description**: Precomputes $\phi(i)$ for all integers $1 \le i \le n$ (suitable up to $n \le 10^6$) using a sieve-based approach based on Euler's product formula.
- **Mathematical Formula**:
  1. Initialize $\phi[i] = i$ for all $0 \le i \le n$.
  2. For each prime $p \in [2, n]$ (identified when $\phi[p] == p$):
     $$\phi[i] \leftarrow \phi[i] - \left\lfloor \frac{\phi[i]}{p} \right\rfloor \quad \forall i \in \{p, 2p, 3p, \dots \le n\}$$
- **Time Complexity**: $\mathcal{O}(n \log(\log n))$
- **Space Complexity**: $\mathcal{O}(n)$

---

## 💻 How to Run

Clone the repository and run any file using Python 3:

```bash
# Clone the repository
git clone https://github.com/Dileep2006/AdvanceMath_cp.git
cd AdvanceMath_cp

# Run any script
python EuclideanAlgo.py
python SeiveofEratosthenes.py
python TotientSieve.py
```
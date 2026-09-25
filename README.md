# Altermath

**Altermath** — A small Python library implementing basic mathematical functions and operations. 
All functions accept an arbitrary amount of numbers and sequentially apply the operation to them.

> Version: 1.0.1

---

## Features

### Arithmetic 

#### `add(*nums)`

Adds the supplied numbers.

```python
add(1, 2, 3, 4)
# 10

add(40, 2)
# 42
```

---

#### `subtract(*nums)`

Sequentially subtracts all numbers from the first one.

```python
subtract(10, 2, 3)
# 5

subtract(10, 7)
# 3
```

---

#### `multiply(*nums)`

Multiplies the supplied numbers.

```python
multiply(2, 3, 4)
# 24

multiply(7)
# 7
```

---

#### `divide(*nums)`

Sequentially divides the first number by the others.

```python
divide(100, 2, 5)
# 10
```

---

#### `mod(*nums)`

Sequentially divides the first number by the others using the modulo operation.

```python
mod(20, 6, 2)
# 0
```

---

#### `fdiv(*nums)`

Sequentially performs integer division.

```python
fdiv(20, 3, 2)
# 3
```

---

### Powers & Roots

#### `square(*nums)`

Squares numbers.

```python
square(2, 3, 4)
# [4, 9, 16]
```

---

#### `cube(*nums)`

Cubes numbers.

```python
cube(2, 3, 4)
# [8, 27, 64]
```

---

#### `power(*nums, exp)`

Raises each supplied number to the specified power.

```python
power(2, 3, exp=2)
# [4, 9]
```

---

#### `sqrt(*nums)`

Calculates the square root.

```python
sqrt(4, 9, 16)
# [2, 3, 4]
```

---

#### `root(*nums, index)`

Calculates root with the specified exponent.

```python
root(27, index=3)
# 3
```

> Note: Index must be a natural number greater than or equal to 2

---

### Constants

```python
from altermath import PI, E, PHI

print(PI) # 3.141592653589793
print(E) # 2.718281828459045
print(PHI) # 1.618033988749895
```

| Constant | Description     | Value           |
| -------- | --------------- | --------------- |
| `PI`     | π               | `~3.141`        |
| `E`      | Euler's number  | `~2.718`        |
| `PHI`    | Golden Ratio    | `~1.618`        |

> Note: Mathematical constants are provided to 15 decimal places.

---

senechka3d

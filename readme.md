# nextperm

A Python library inspired by C++ STL and Java Collections that provides utilities for next permutation, combinations, sorting helpers, and more.

## 🚀 Features

- `next_permutation`, `prev_permutation`
- `rotate_left`, `rotate_right`
- `is_sorted`, `is_sorted_until`
- `lower_bound`, `upper_bound`
- `nth_permutation`, `count_permutations`
- `nCr`, `nPr`, `factorial`
- `shuffle`, `swap`, `reverse`

## 🧪 Example Usage

```python
from nextperm import next_permutation, nth_permutation

print(next_permutation([1, 2, 3]))  # [1, 3, 2]
print(nth_permutation([1, 2, 3], 4))  # [2, 3, 1]

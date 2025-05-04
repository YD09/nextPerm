import random
import math
from itertools import permutations, combinations

def next_permutation(seq):
    seq = list(seq)
    i = len(seq) - 2
    while i >= 0 and seq[i] >= seq[i + 1]:
        i -= 1
    if i >= 0:
        j = len(seq) - 1
        while seq[j] <= seq[i]:
            j -= 1
        seq[i], seq[j] = seq[j], seq[i]
    seq[i + 1:] = reversed(seq[i + 1:])
    return seq

def prev_permutation(seq):
    seq = list(seq)
    i = len(seq) - 2
    while i >= 0 and seq[i] <= seq[i + 1]:
        i -= 1
    if i >= 0:
        j = len(seq) - 1
        while seq[j] >= seq[i]:
            j -= 1
        seq[i], seq[j] = seq[j], seq[i]
    seq[i + 1:] = reversed(seq[i + 1:])
    return seq

def is_sorted(seq):
    return all(seq[i] <= seq[i + 1] for i in range(len(seq) - 1))

def is_sorted_until(seq):
    for i in range(len(seq) - 1):
        if seq[i] > seq[i + 1]:
            return i + 1
    return len(seq)

def rotate_left(seq, k):
    k %= len(seq)
    return seq[k:] + seq[:k]

def rotate_right(seq, k):
    k %= len(seq)
    return seq[-k:] + seq[:-k]

def lower_bound(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

def upper_bound(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low

def count_permutations(seq):
    from collections import Counter
    freq = Counter(seq)
    denom = 1
    for count in freq.values():
        denom *= math.factorial(count)
    return math.factorial(len(seq)) // denom

def nth_permutation(seq, n):
    from math import factorial
    seq = sorted(seq)
    result = []
    n = n % factorial(len(seq))
    while seq:
        f = factorial(len(seq) - 1)
        i = n // f
        result.append(seq.pop(i))
        n %= f
    return result

def reverse(seq):
    return list(reversed(seq))

def shuffle(seq):
    seq = list(seq)
    random.shuffle(seq)
    return seq

def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]
    return seq


def generate_combinations(seq, r):
    return list(combinations(seq, r))

def factorial(n):
    return math.factorial(n)

def nCr(n, r):
    return math.comb(n, r)

def nPr(n, r):
    return math.perm(n, r)

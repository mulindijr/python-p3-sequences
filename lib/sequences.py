#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    else:
        a, b = 0, 1
        fibonacci_sequence = [a]
        for _ in range(length - 1):
            a, b = b, a + b
            fibonacci_sequence.append(a)
        print(fibonacci_sequence)

print_fibonacci(0)


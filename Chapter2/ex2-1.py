"""
Binary Search(BS)
"""


def bs(n, low, high):
    turns = 0

    while high >= low:
        turns += 1

        mid = (low + high) // 2

        if n == mid:
            return turns
        elif mid < n:
            low = mid + 1
        else:
            high = mid - 1

    return turns


low = 1
high = int(1e+6)

print(bs(n=5, low=low, high=high))

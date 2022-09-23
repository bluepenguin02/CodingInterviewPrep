"""
10.4: Sorted Search, No Size
"""

def bin_search_no_size(a: list, x: int) -> int:
    if x < 0:
        return -1
    hi = growing_bin_search(a, x)
    return shrinking_bin_search(a, hi//2, hi, x)


def growing_bin_search(a: list, x: int) -> int:
    i = 1
    val = listy(a, i)
    while -1 < val < x:
        i *= 2
        val = listy(a, i)
    return i


def listy(a: list, i: int) -> int:
    if i >= len(a):
        return -1
    else:
        return a[i]


def shrinking_bin_search(a: list, lo: int, hi: int, x: int) -> int:
    # Returns -1 if not found.  Alternatively, we could return lo,
    # which tells us where to put the value if we wanted to.
    while lo <= hi:
        mid = (lo + hi) // 2
        val = listy(a, mid)
        if val == x:
            return mid
        elif -1 < val < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == '__main__':
    testy = list(range(10))
    print(bin_search_no_size(testy, 0))

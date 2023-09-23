"""
16.16: Sub Sort
"""

def sub_sort(array: list) -> tuple:
    if not array:
        return None
    
    if is_sorted(array):
        return 0, 0
    
    left = get_seq_left_idx(array)
    right = get_seq_right_idx(array)
    return left, right

def is_sorted(array: list) -> bool:
    if len(array) == 1:
        return True
    
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

def get_seq_left_idx(array):
    left = 0
    while left < len(array)-1 and array[left] <= array[left+1]:
        left += 1
    seq_min = min(array[left:])
    
    left = 0
    while array[left] <= seq_min:
        left += 1
    return left

def get_seq_right_idx(array):
    right = len(array) - 1
    while 0 < right and array[right-1] <= array[right]:
        right -= 1
    seq_max = max(array[:right])
    
    right = len(array) - 1
    while array[right] >= seq_max:
        right -= 1
    return right


if __name__ == '__main__':
    # test = list(range(10))
    # test.reverse()
    test = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    # test = []
    # test = [1, 2, 3, 4, 5, 6, 1]
    print(sub_sort(test))
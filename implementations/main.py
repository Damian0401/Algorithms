from collections.abc import Callable
import random
import time

from numpy import number
from sort import (
    bubble_sort, 
    quick_sort, 
    cocktail_sort, 
    insert_sort, 
    selection_sort, 
    comb_sort,
    counting_sort,
    bucket_sort
)

# analyze sort function
def analyze_sort(func: Callable[[]], data: list, display: bool = True) -> None:
    print(f'>>>>> {func.__name__} <<<<< START')
    if display:
        print(f'before: {data}')
    time = measure_time(func, data)
    if display:
        print(f'after: {data}')
    print(f'number of elements: {len(data)}')
    print(f'sorted: {is_sorted(data)}')
    print(f'time: {time:.3f}ms')
    print(f'>>>>> {func.__name__} <<<<< STOP')
    print('')

# measure time of execution a function
def measure_time(func: Callable[[]], data: list) -> float:
    start = time.time()
    func(data)
    stop = time.time()
    return (stop - start) * 1000

# check if data are sorted
def is_sorted(data: list) -> bool:
    list_len = len(data)
    if list_len < 2:
        return True
    i = 1
    while i < list_len:
        if (data[i] < data[i-1]):
            return False
        i += 1
    return True

# generate random data
def generate_data(start_range: int, end_range: int, amount: int, unique: bool = False) -> list:
    if unique:
        return random.sample(range(start_range, end_range), amount)
    return [random.randint(start_range, end_range) for i in range(amount)]

# run sort analyze
def analyze_sorts(sorts: list,start_range: number = 0, end_range: number = 5000, amount: number = 2000, unique: bool = False, display: bool = False):
    data = generate_data(start_range, end_range, amount, unique)
    for sort in sorts:
        analyze_sort(sort, data.copy(), display)

# main function
def main():
    sorts = [bubble_sort, cocktail_sort, insert_sort, selection_sort, comb_sort, quick_sort, counting_sort, bucket_sort]
    analyze_sorts(sorts)

# call main function if necessary
if(__name__ == '__main__'):
    main()

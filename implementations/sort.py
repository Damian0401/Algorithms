
# bubble sort
from numpy import number


def bubble_sort(arr: list):
    length = len(arr) - 1
    for i in range(length):
        for j in range(length - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# quick sort
def quick_sort(arr: list):
    quick_sort_recursive_part(arr, 0, len(arr) - 1)

# part of quick sort algorithm
def quick_sort_recursive_part(arr: list, low: int, high: int):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort_recursive_part(arr, low, pivot - 1)
        quick_sort_recursive_part(arr, pivot + 1, high)

# part of quick sort algorithm
def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# cocktail sort
def cocktail_sort(arr: list):
    bottom = 0
    top = len(arr) - 1
    is_sorted = False
    while is_sorted is False:
        is_sorted = True
        for i in range(bottom, top):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        if is_sorted:
            break
        top -= 1
        for i in range(top, bottom, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                is_sorted = False
        bottom += 1


# insert sort
def insert_sort(arr: list):
    sorted_list = [arr[0]]
    is_added = False
    for i in range(1, len(arr)):
        is_added = False
        for j in range(len(sorted_list)):
            if arr[i] <= sorted_list[j]:
                sorted_list.insert(j, arr[i])
                is_added = True
                break
        if is_added is False:
            sorted_list.append(arr[i])
    arr.clear()
    arr.extend(sorted_list)

# selection sort
def selection_sort(arr: list):
    for i in range(len(arr)):
        min_value = min(arr[i:])
        min_index = arr[i:].index(min_value)
        arr[i], arr[min_index + i] = arr[min_index + i], arr[i]

# comb sort
def comb_sort(arr: list):
    length = get_length(len(arr))
    max_index = len(arr)
    swapped = True
    while length > 1 or swapped:
        swapped = False
        for i in range(0, max_index - length):
            if arr[i] > arr[i + length]:
                arr[i], arr[i + length] = arr[i + length], arr[i]
                swapped = True
        length = get_length(length)

# part of comb sort
def get_length(length: number):
    new_length = int(length // 1.3)
    if new_length > 1:
        return new_length
    return 1

# counting sort
def counting_sort(arr: list):
    min_element = min(arr)
    max_element = max(arr)
    hist = {}
    for i in range(min_element, max_element + 1):
        hist[i] = 0
    for i in arr:
        hist[i] += 1
    sorted_list = []
    for key, value in hist.items():
        for i in range(value):
            sorted_list.append(key)
    arr.clear()
    arr.extend(sorted_list)

# radix sort
def radix_sort(arr: list):
    print('TODO')

# bucket sort
def bucket_sort(arr: list):
    length = len(arr)
    max_value = max(arr)
    min_value = min(arr)
    interval = (max_value - min_value) / length
    buckets = []
    for i in range(length):
        buckets.append([])
    for i in arr:
        index = int((i - min_value) // interval)
        if index == length:
            buckets[length - 1].append(i)
            continue
        buckets[index].append(i)
    for bucket in buckets:
        quick_sort(bucket)
    arr.clear()
    for bucket in buckets:
        arr.extend(bucket)
    
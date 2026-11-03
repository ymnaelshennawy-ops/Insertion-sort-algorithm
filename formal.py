import time
import random

def insertion_sort(arr):
    A = list(arr)
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def benchmark():
    n = 1000
    data_random = [random.randint(1, 10000) for _ in range(n)]
    data_sorted = list(range(n))
    data_reverse = list(range(n, 0, -1))

    datasets = {
        "Random": data_random,
        "Sorted": data_sorted,
        "Reverse": data_reverse
    }

    for name, data in datasets.items():
        print(f"--- Dataset: {name} ---")
        
        start = time.time()
        insertion_sort(data)
        print(f"Insertion Sort: {time.time() - start:.5f} seconds")
        
        start = time.time()
        merge_sort(data)
        print(f"Merge Sort: {time.time() - start:.5f} seconds")
        
        start = time.time()
        quick_sort(data)
        print(f"Quick Sort: {time.time() - start:.5f} seconds")
        
        start = time.time()
        sorted(data)
        print(f"Python sorted(): {time.time() - start:.5f} seconds\n")

if __name__ == "__main__":
    benchmark()
import time
import random

def heapify(arr, n, i, counter):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n:
        counter[0] += 1
        if arr[left] > arr[largest]:
            largest = left
            
    if right < n:
        counter[0] += 1
        if arr[right] > arr[largest]:
            largest = right
            
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, counter)

def heap_sort(arr):
    A = list(arr)
    n = len(A)
    counter = [0]
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i, counter)
        
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0, counter)
        
    return A, counter[0]

def test_cases():
    test_inputs = [
        [],
        [5],
        [3, 3, 1, 2, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
    
    for idx, case in enumerate(test_inputs):
        sorted_arr, comps = heap_sort(case)
        print(f"Test {idx+1}: Sorted: {sorted_arr} | Comparisons: {comps}")

def measure_performance():
    n = 1000
    data = [random.randint(1, 10000) for _ in range(n)]
    
    start = time.time()
    heap_sort(data)
    print(f"Heap Sort Time for n={n}: {time.time() - start:.5f} seconds")

if __name__ == "__main__":
    test_cases()
    measure_performance()
import time

def time_algorithm(func, arr):
    start = time.time()
    sorted_arr = func(arr)
    end = time.time()
    return end - start, sorted_arr

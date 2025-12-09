import time

def my_function():
    # Simulate some work
    sum(range(10**8))

start_time = time.perf_counter()
my_function()
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.6f} seconds")
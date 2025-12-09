import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter
from datetime import timedelta


def sieve_of_eratosthenes_optimized(limit):
    """
    Generates all prime numbers up to 'limit' using an optimized 
    Sieve of Eratosthenes, utilizing numpy for speed.
    """
    if limit < 2:
        return []
    
    # We only need to store odd numbers from 3 onwards
    # Index i corresponds to number 2*i + 3
    size = (limit + 1) // 2
    is_prime = np.ones(size, dtype=bool)
    
    # The first odd number is 3, start p from 3
    p = 3
    while p * p <= limit:
        # If is_prime[i] is True, then p is prime
        if is_prime[(p - 3) // 2]:
            # Mark multiples of p as non-prime. 
            # Start from p*p (lower multiples were already marked by smaller primes)
            # and increment by 2*p to only mark odd multiples.
            start_index = (p * p - 3) // 2
            # Use slicing for performance
            is_prime[start_index::p] = False
        
        # Move to the next odd number
        p += 2
        
    # Collect the primes
    primes = [2]
    # Use numpy where to quickly get indices of True values
    odd_primes = 2 * np.where(is_prime)[0] + 3
    primes.extend(odd_primes)
    
    # Filter out any primes that might exceed the limit due to array sizing
    return [p for p in primes if p <= limit]



# Find first 50 primes
x = int(input("Enter the number of prime numbers to plot: "))

start_time = perf_counter() # start timer

primes = sieve_of_eratosthenes_optimized(x)

end_time = perf_counter() # end timer


elapsed_secs = end_time - start_time # calculate elapsed time

duration = timedelta(seconds=elapsed_secs) # format elapsed time
print(f"Found {len(primes)} primes up to {x} in {duration}.") # print results

# add input to prevent timeout
input("Press Enter to create graph...")

start_time = perf_counter() # start timer for graphing

# Create y-values (index + 1 for each prime)
y_values = list(range(1, len(primes) + 1))

# Plot
plt.figure(figsize=(12, 6))
plt.scatter(primes, y_values, alpha=0.6)
plt.xlabel('Prime Number')
plt.ylabel('Prime Count')
plt.title(f'First {x} Prime Numbers')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('prime_graph.png')
plt.show()

end_time = perf_counter() # end timer for graphing

elapsed_secs = end_time - start_time # calculate elapsed time for graphing
duration = timedelta(seconds=elapsed_secs) # format elapsed time
print(f"Graph created in {duration}.") # print results for graphing
print("Graph saved as 'prime_graph.png'.")
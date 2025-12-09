import matplotlib.pyplot as plt

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_first_x_primes(x):
    primes = []
    n = 2
    while len(primes) < x:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes

# Find first 50 primes
x = 50
primes = find_first_x_primes(x)

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
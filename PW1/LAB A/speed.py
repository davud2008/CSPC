import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4

start = time.perf_counter()
simulate_loop(N0, lam)
loop_time = time.perf_counter() - start

start = time.perf_counter()
simulate(N0, lam)
numpy_time = time.perf_counter() - start

speed_up = loop_time / numpy_time

print(f"Python loop: {loop_time:.4f} s")
print(f"NumPy:       {numpy_time:.4f} s")
print(f"NumPy is {speed_up:.2f}x faster")
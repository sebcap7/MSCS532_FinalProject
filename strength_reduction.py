import random
import math
import time
from statistics import mean


# --------------------------------------------------
# Configuration
# --------------------------------------------------

NUM_POINTS = 1_000_000
THRESHOLD = 50
NUM_TRIALS = 5


# --------------------------------------------------
# Generate Dataset
# --------------------------------------------------

print("Generating random dataset...")

points = [
    (
        random.uniform(-100, 100),
        random.uniform(-100, 100)
    )
    for _ in range(NUM_POINTS)
]

print(f"Generated {NUM_POINTS:,} points.\n")


# --------------------------------------------------
# Version 1
# Uses expensive sqrt() operation
# --------------------------------------------------

def expensive_version(points, threshold):
    inside_count = 0

    for x, y in points:
        distance = math.sqrt(x * x + y * y)

        if distance < threshold:
            inside_count += 1

    return inside_count


# --------------------------------------------------
# Version 2
# Strength reduction
# Removes sqrt()
# --------------------------------------------------

def optimized_version(points, threshold):
    inside_count = 0

    threshold_squared = threshold * threshold

    for x, y in points:
        distance_squared = x * x + y * y

        if distance_squared < threshold_squared:
            inside_count += 1

    return inside_count


# --------------------------------------------------
# Benchmark Helper
# --------------------------------------------------

def benchmark(function, points, threshold, trials):

    execution_times = []
    result = None

    for trial in range(trials):

        start = time.perf_counter()

        result = function(points, threshold)

        elapsed = time.perf_counter() - start

        execution_times.append(elapsed)

        print(
            f"{function.__name__} "
            f"Trial {trial + 1}: "
            f"{elapsed:.4f} sec"
        )

    return result, execution_times


# --------------------------------------------------
# Run Benchmarks
# --------------------------------------------------

print("Running expensive version...\n")

count1, expensive_times = benchmark(
    expensive_version,
    points,
    THRESHOLD,
    NUM_TRIALS
)


print("\nRunning optimized version...\n")

count2, optimized_times = benchmark(
    optimized_version,
    points,
    THRESHOLD,
    NUM_TRIALS
)


# --------------------------------------------------
# Calculate Statistics
# --------------------------------------------------

avg_expensive = mean(expensive_times)
avg_optimized = mean(optimized_times)

improvement = (
    (avg_expensive - avg_optimized)
    / avg_expensive
) * 100


# --------------------------------------------------
# Display Results
# --------------------------------------------------

print("\n" + "=" * 50)
print("FINAL RESULTS")
print("=" * 50)

print(f"Points Tested: {NUM_POINTS:,}")
print(f"Threshold: {THRESHOLD}")

print()

print(f"Expensive Version Count : {count1}")
print(f"Optimized Version Count : {count2}")

print()

print(
    f"Average Runtime (sqrt) : "
    f"{avg_expensive:.4f} sec"
)

print(
    f"Average Runtime (reduced) : "
    f"{avg_optimized:.4f} sec"
)

print()

print(
    f"Performance Improvement : "
    f"{improvement:.2f}%"
)

print()

if count1 == count2:
    print(
        "Validation Successful: "
        "Both implementations produced identical results."
    )
else:
    print(
        "Validation Failed: "
        "Results differ."
    )

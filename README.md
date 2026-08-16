Optimization Technique: Operator Strength Reduction in High-Performance Computing
=================================================================================

Overview
--------
This project demonstrates Operator Strength Reduction, an optimization technique
discussed in the research paper "An Empirical Study of High Performance Computing
(HPC) Performance Bugs."

The goal is to demonstrate how replacing a computationally expensive mathematical
operation with a less expensive equivalent can improve performance while
maintaining identical results.

The program compares two approaches:

1. Expensive Version
   - Uses the math.sqrt() function to calculate Euclidean distance.
   - Performs a square-root operation for every point.

2. Optimized Version
   - Eliminates the square-root operation.
   - Uses squared-distance comparisons instead.
   - Demonstrates operator strength reduction.


Requirements
------------
- Python 3.8 or newer
- No external libraries required

The program only uses standard Python libraries:
- random
- math
- time
- statistics


Files
-----
strength_reduction.py
README.txt


How to Run
----------

Linux / macOS:

python3 strength_reduction.py

Windows:

python strength_reduction.py


Program Configuration
---------------------
The following variables can be modified near the top of the script:

NUM_POINTS = 1_000_000
THRESHOLD = 50
NUM_TRIALS = 5


Parameter Descriptions
----------------------

NUM_POINTS
Number of random points generated for testing.

THRESHOLD
Distance threshold used in the comparison.

NUM_TRIALS
Number of benchmark runs performed for each version.


Program Workflow
----------------
1. Generate one million random points.
2. Execute the baseline implementation five times.
3. Execute the optimized implementation five times.
4. Calculate the average execution time for each version.
5. Measure the performance improvement.
6. Verify that both implementations produce identical results.


Optimization Technique
----------------------

Baseline Approach:

distance = math.sqrt(x * x + y * y)

The baseline implementation calculates the Euclidean distance using the
square-root operation.

Optimized Approach:

distance_squared = x * x + y * y
threshold_squared = threshold * threshold

The optimized implementation compares squared distances instead of calculating
the actual distance.

Because both values are non-negative, the comparison:

distance < threshold

is mathematically equivalent to:

distance_squared < threshold_squared

This allows the program to avoid the square-root operation while preserving
correctness.


Sample Results
--------------

Generating random dataset...
Generated 1,000,000 points.

Running expensive version...

expensive_version Trial 1: 0.1187 sec
expensive_version Trial 2: 0.1171 sec
expensive_version Trial 3: 0.1335 sec
expensive_version Trial 4: 0.1095 sec
expensive_version Trial 5: 0.1086 sec

Running optimized version...

optimized_version Trial 1: 0.0774 sec
optimized_version Trial 2: 0.0854 sec
optimized_version Trial 3: 0.0799 sec
optimized_version Trial 4: 0.0909 sec
optimized_version Trial 5: 0.0784 sec


Observed Results
----------------

Points Tested:
1,000,000

Threshold:
50

Expensive Version Count:
196,241

Optimized Version Count:
196,241

Average Runtime (sqrt):
0.1175 seconds

Average Runtime (reduced):
0.0824 seconds

Performance Improvement:
29.87%


Validation
----------

Validation Successful:
Both implementations produced identical results.


Conclusion
----------

The optimized implementation achieved a 29.87% performance improvement while
producing identical results to the baseline implementation.

This experiment demonstrates the effectiveness of operator strength reduction.
By replacing an expensive mathematical operation, such as square root, with a
computationally cheaper equivalent operation, the program can improve execution
efficiency without changing the correctness of the result.

The benchmark shows that removing the square-root calculation reduced the
average runtime from 0.1175 seconds to 0.0824 seconds for one million points.

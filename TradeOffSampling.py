import numpy as np

np.random.seed(42)  # Setting seed for reproducibility

population_size = 1000000
p_plus_one = 0.52
p_minus_one = 0.48
num_experiments = 100

# Function to simulate an experiment and calculate the probability of +1 being the majority
def simulate_experiment(sample_size):
    count_majority_plus_one = 0
    for _ in range(num_experiments):
        sample = np.random.choice([1, -1], size=sample_size, p=[p_plus_one, p_minus_one])
        count_plus_one = np.sum(sample == 1)
        if count_plus_one > sample_size / 2:
            count_majority_plus_one += 1
    return count_majority_plus_one / num_experiments

# Perform experiments for sample sizes (a), (b), and (c)
sample_sizes = [20, 100, 400]

for size in sample_sizes:
    probability = simulate_experiment(size)
    print(f"Sample Size: {size}, Average Probability of +1 being the Majority: {probability:.4f}")

# Find the sample size needed for the probability to become 0.9
target_probability = 0.9
required_sample_size = 1
while simulate_experiment(required_sample_size) < target_probability:
    required_sample_size += 1

print(f"\nSample Size needed for Probability 0.9: {required_sample_size}")

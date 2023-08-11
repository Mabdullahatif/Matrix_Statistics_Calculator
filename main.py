import numpy as np

def calculate(nums):
    if len(nums) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the list into a 3x3 numpy array
    matrix = np.array(nums).reshape(3, 3)

    # Calculate mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    }

    return calculations

# Define the list of nine numbers for analysis
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Calculate mean, variance, and standard deviation
calculations = calculate(nums)

# Print the calculations
print("Mean, Variance, and Standard Deviation:")
for key, values in calculations.items():
    print(key)
    for i, val in enumerate(values):
        print(f"Axis {i}: {val}")
    print("Flattened:", values[2])
    print()

import numpy as np

# Create a 2D array
a = np.array([[10, 20], [30, 40]])

# Add character labels
rows = ['A', 'B']
columns = ['X', 'Y']

# Print array with labels
print("   ", columns)
for i in range(len(a)):
    print(rows[i], a[i])


import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate a random array of 50 numbers between 0-100
array_random = np.random.randint(0, 101, size=50)

# Step 2: Calculate mean, median, and standard deviation
mean_value = np.mean(array_random)
median_value = np.median(array_random)
std_dev = np.std(array_random)

# Step 3: Numbers above the mean
above_mean = array_random[array_random > mean_value]

# Step 4: New array with even numbers only
even_numbers = array_random[array_random % 2 == 0]

# Step 5: Find the minimum and maximum of the even numbers array
min_even = np.min(even_numbers)
max_even = np.max(even_numbers)

# Step 6: Reshape the first array into a 5x10 matrix
matrix_5x10 = array_random.reshape(5, 10)

# Step 7: Transpose and calculate the sum of each row
transposed_matrix = matrix_5x10.T
row_sums = np.sum(transposed_matrix, axis=1)

# Step 8: Plot a histogram of the first array
plt.hist(array_random, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.title('Histogram of the Random Array')
plt.show()

# Displaying results
print("Array Random:", array_random)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev)
print("Above Mean:", above_mean)
print("Even Numbers:", even_numbers)
print("Min Even:", min_even)
print("Max Even:", max_even)
print("5x10 Matrix:\n", matrix_5x10)
print("Transposed Matrix:\n", transposed_matrix)
print("Row Sums:", row_sums)

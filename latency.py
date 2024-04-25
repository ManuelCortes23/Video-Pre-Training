import pandas as pd

# Load the CSV file
data = pd.read_csv('image_save_interval.csv', header=None, names=['Timestamp', 'Interval'])

# Calculate the mean and standard deviation of the intervals
mean_interval = data['Interval'].mean()
std_interval = data['Interval'].std()

# Print the results
print(f"Mean Interval: {mean_interval} seconds")
print(f"Standard Deviation of Intervals: {std_interval} seconds")

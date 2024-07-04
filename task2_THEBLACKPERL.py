import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
# Example: Loading a CSV file named 'dataset.csv'
df = pd.read_csv('dataset.csv')

# Step 2: Data Exploration
# Example: Display the first few rows of the dataset
print("First few rows:")
print(df.head())

# Example: Filter data based on a condition
filtered_data = df[df['column_name'] > 100]

# Example: Sort data by a column
sorted_data = df.sort_values(by='column_name')

# Example: Group data by a column and calculate mean
grouped_data = df.groupby('category_column')['numeric_column'].mean()

# Step 3: Calculate Summary Statistics
# Example: Calculate mean, median, and standard deviation
mean_value = df['numeric_column'].mean()
median_value = df['numeric_column'].median()
std_value = df['numeric_column'].std()

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_value)

# Step 4: Data Visualization
# Example: Histogram
plt.figure(figsize=(8, 6))
plt.hist(df['numeric_column'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Numeric Column')
plt.ylabel('Frequency')
plt.title('Histogram of Numeric Column')
plt.show()

# Example: Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['column1'], df['column2'], color='green')
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.title('Scatter plot of Column 1 vs Column 2')
plt.show()

# Example: Heatmap (using Seaborn)
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

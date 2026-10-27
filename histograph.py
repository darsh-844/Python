import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]

# Data
salaries = [
   50000, 60000, 55000, 70000, 65000,
   80000, 75000, 90000, 85000, 95000, 
   32000, 21320, 13330, 99999, 150000
]

# Histogram
plt.figure(figsize=(8,5))
plt.hist(salaries, bins=8, color='purple', edgecolor='black')

# Title and Labels
plt.title('Salary Distribution')
plt.xlabel('Salary Range ($)')
plt.ylabel('Number of Employees')

# Grid
plt.grid(axis='y', alpha=0.75)

# Show Plot
plt.show()
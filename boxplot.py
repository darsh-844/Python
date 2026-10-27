import matplotlib.pyplot as plt  

# Data
it_salaries = [120000, 70000, 89000, 69000, 217000]
hr_salaries = [98300, 30000, 89000, 77000, 12000]
finance_salaries = [38000, 120002, 69000, 192300]
salary_data = [it_salaries, hr_salaries, finance_salaries]

# Boxplot
plt.figure(figsize=(8, 5))
plt.boxplot(
    salary_data,
    labels=["IT", "HR", "FINANCE"]
)

# Title and Labels
plt.title("Salary Distribution by Department", fontsize=14, fontweight='bold')
plt.ylabel("Salary (USD)", fontsize=12)

# Grid
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Show Plot
plt.show()

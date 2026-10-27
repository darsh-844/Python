import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1000, 1200, 1500, 1300, 1700, 1600, 1800, 2000, 2200, 2100, 2300, 2500]

# Line Chart
plt.plot(months, sales, marker='o', linestyle='-', color='b')

# Title and Labels
plt.title('Monthly Sales Trend')
plt.xlabel('Months')
plt.ylabel('Sales ($)')

# Show Grid
plt.grid(True)

# Show Plot
plt.show()


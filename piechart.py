import matplotlib.pyplot as plt

# Data
categories = ['Electronics', 'Clothing', 'Grocery', 'Furniture', 'Toys', 'Books']
sales = [25000, 15000, 30000, 10000, 10000, 10000]

# Pie Chart
plt.figure(figsize=(7,7))
plt.pie(sales, labels=categories, autopct='%1.1f%%')

# Title
plt.title('Category-Wise Sales Distribution')

# Show Plot
plt.show()

import matplotlib.pyplot as plt     # pyright: ignore[reportMissingModuleSource]

# Region-Wise Data
regions = ['North', 'South', 'East', 'West']
region_sales = [5000, 7000, 6000, 8000]

# Bar Chart
plt.bar(regions, region_sales, color=['red', 'green', 'blue', 'orange'])

# Title and Labels
plt.title('Region-Wise Sales Data')
plt.xlabel('Regions')
plt.ylabel('Sales ($)')

# Show Plot
plt.show()
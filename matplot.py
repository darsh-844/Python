import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


tips = px.data.tips()      # restaurant bills and tips
iris = px.data.iris()      # flower measurements
stocks = px.data.stocks()  # weekly stock prices

tips.head()

# ==================== Task 1: Line Chart (Matplotlib) ====================
print("------------------------ Task 1 ------------------------")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [12, 15, 14, 20, 24, 22]  # in thousands

plt.figure(figsize=(8, 4))
plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Trend')
plt.xlabel('Months')
plt.ylabel('Sales (in thousands)')
plt.grid(True)
plt.show()

max_sales_month = months[sales.index(max(sales))]
print(f"Highest Sales observed in the month of {max_sales_month} with a value of {max(sales)}k\n")


# ==================== Task 2: Bar Chart (Matplotlib) ====================
print("------------------------ Task 2 ------------------------")
avg_tip = tips.groupby("day")["tip"].mean().reindex(["Thur", "Fri", "Sat", "Sun"])
print(avg_tip)

plt.figure(figsize=(8, 5))
plt.bar(avg_tip.index, avg_tip.values, color='skyblue', edgecolor='black')
plt.title('Average Tips By Day')
plt.xlabel('Day')
plt.ylabel('Average Tip')
plt.show()

print(f"Highest Average Tip observed on {avg_tip.idxmax()} with a value of {avg_tip.max():.2f}\n")


# ==================== Task 3: Histogram & Scatter Plot ====================
print("------------------------ Task 3 ------------------------")
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Left: Histogram of total_bill with 10 bins
axes[0].hist(tips['total_bill'], bins=10, color="lightgreen", edgecolor="black")
axes[0].set_title("Total Bill Distribution")
axes[0].set_xlabel("Total Bill ($)")
axes[0].set_ylabel("Frequency")

# Right: Scatter plot of total_bill vs tip
axes[1].scatter(tips['total_bill'], tips['tip'], color="orange", alpha=0.7)
axes[1].set_title("Total Bill vs Tip")
axes[1].set_xlabel("Total Bill ($)")
axes[1].set_ylabel("Tip ($)")
axes[1].grid(True)

plt.tight_layout()
plt.savefig("tips_plots.png", dpi=150)
plt.show()

print("Description: Most common bill range is between $10 and $20. There is a positive linear relationship between bill and tip (higher bills generally result in higher tips).\n")


# ==================== Task 4: Count Plot & Bar Plot (Seaborn) ====================
print("------------------------ Task 4 ------------------------")
plt.figure(figsize=(8, 4))
sns.countplot(data=tips, x="day", order=["Thur", "Fri", "Sat", "Sun"], palette="Set2")
plt.title("Number of Customers on Each Day")
plt.xlabel("Day")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8, 4))
sns.barplot(data=tips, x="day", y="total_bill", order=["Thur", "Fri", "Sat", "Sun"], palette="Set2")
plt.title("Average Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Total Bill ($)")
plt.show()

customer_counts = tips['day'].value_counts()
avg_bill_day = tips.groupby('day')['total_bill'].mean()
print(f"Day with the most customers: {customer_counts.idxmax()}")
print(f"Day with the highest average bill: {avg_bill_day.idxmax()}\n")


# ==================== Task 5: Box Plot ====================
print("------------------------ Task 5 ------------------------")
plt.figure(figsize=(8, 4))
sns.boxplot(data=tips, x="day", y="total_bill", order=["Thur", "Fri", "Sat", "Sun"])
plt.title("Total Bill Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.show()

plt.figure(figsize=(8, 4))
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex", order=["Thur", "Fri", "Sat", "Sun"])
plt.title("Total Bill Distribution by Day and Gender")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")
plt.legend(title="Sex")
plt.show()

median_bill = tips.groupby('day')['total_bill'].median()
print(f"-> Median bills by day:\n{median_bill}")
print("Note: Dots beyond whiskers represent statistical outliers (unusually high bills).")
print("Difference with hue='sex': Males generally have higher median bills and wider interquartile ranges across most days compared to females.\n")


# ==================== Task 6: Scatter Plot with Hue & Style ====================
print("------------------------ Task 6 ------------------------")
plt.figure(figsize=(8, 5))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="smoker", style="time")
plt.title("Total Bill vs Tip by Smoker Status and Time")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

print("Smoker vs Non-smoker insight: Smokers and non-smokers exhibit very similar tipping trends relative to the total bill amount.\n")


# ==================== Task 7: Pair Plot ====================
print("------------------------ Task 7 ------------------------")

sns.pairplot(iris, hue="species", vars=["sepal_length", "sepal_width", "petal_length", "petal_width"])
plt.show()

print("Petal length and petal width separate the three species best.")
print("Setosa is the easiest species to identify due to its distinctly smaller and well-separated petal dimensions.\n")


# ==================== Task 8: Interactive Scatter Plot (Plotly) ====================
print("------------------------ Task 8 ------------------------")
fig8 = px.scatter(
    tips, x="total_bill", y="tip", color="day", size="size",
    hover_data=["sex", "time"], title="Bill vs Tip (Interactive)"
)
fig8.show()

print("Two things you can do in Plotly that Matplotlib can't: Hover over individual data points to view metadata (sex, time), and dynamically toggle categories on/off by clicking legend items.\n")


# ==================== Task 9: Interactive Box Plot & Histogram ====================
print("------------------------ Task 9 ------------------------")
fig9_box = px.box(tips, x="day", y="total_bill", color="sex", title="Interactive Box Plot")
fig9_box.show()

fig9_hist = px.histogram(tips, x="total_bill", color="time", nbins=15, title="Interactive Histogram")
fig9_hist.show()

print("Dinner generally has larger bills and higher maximums compared to Lunch.\n")


# ==================== Task 10: Line Chart with Range Slider ====================
print("------------------------ Task 10 ------------------------")
fig10 = px.line(stocks, x="date", y=["GOOG", "AAPL", "AMZN"], title="Stock Prices with Range Slider")
fig10.update_xaxes(rangeslider_visible=True)
fig10.show()

print("MSFT/GOOG/AAPL/AMZN stock growth check can be evaluated directly via the interactive range slider.\n")


# ==================== Task 11: Comparing Libraries ====================
print("------------------------ Task 11 ------------------------")
comparison_table = pd.DataFrame({
    "Library": ["Matplotlib", "Seaborn", "Plotly"],
    "Ease of Use": ["Medium", "Easy", "Medium"],
    "Interactive Charts": ["No", "No", "Yes"],
    "Best Used For": ["Fine-tuning & customization", "Statistical data visualization", "Web apps & interactive dashboards"]
})
print(comparison_table.to_markdown(index=False))

print("\nLab Report Recommendation: Choose **Matplotlib** or **Seaborn** because they export cleanly to static vector formats (like PDF or high-DPI PNG) required for academic/printed reports.")
print("Web Page Recommendation: Choose **Plotly** because its built-in HTML/JavaScript interactivity (hover tooltips, zooming, range sliders) provides an engaging user experience.")
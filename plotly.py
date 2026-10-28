import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

gap = px.data.gapminder()
gap_2007 = gap[gap['year'] == 2007 ]        #only the latest year

gap.head()

# ==================== Task 1 ====================
top10= gap_2007.nlargest(10,'pop')
top10 = top10.copy()
top10['Population_Million'] = top10['pop'] / 1000000
plt.figure(figsize=(12,6))
plt.barh(top10['country'],top10['Population_Million'],color='red')
plt.title('Top 10 countries by Population (2007)')
plt.xlabel('Population in Millions')
plt.ylabel('Country')
plt.tight_layout()
plt.show()


# ==================== Task 2 ====================
g = gap[gap["year"].isin([1952, 2007])].groupby(["continent", "year"])["lifeExp"].mean().unstack()
print(g)

g.plot(kind="bar", figsize=(10, 6), colormap="Set2")
plt.title("Average Life Expectancy by Continent (1952 vs 2007)")
plt.xlabel("Continent")
plt.ylabel("Average Life Expectancy (Years)")
plt.xticks(rotation=0)
plt.legend(title="Year")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

print("Asia improved the most between 1952 and 2007, showing the largest gain in average life expectancy.\n")



# ==================== Task 3 ====================
countries = ["India", "China", "Brazil", "United States"]
subset_countries = gap[gap["country"].isin(countries)]

plt.figure(figsize=(10, 6))
sns.lineplot(data=subset_countries, x="year", y="lifeExp", hue="country", marker="o", linewidth=2.5)
plt.title("Life Expectancy Change Over Time (1952-2007)")
plt.xlabel("Year")
plt.ylabel("Life Expectancy (Years)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(title="Country")
plt.show()

print("Lowest starting life expectancy: India (in 1952).")
print("Improved the fastest: China")
print("Why line chart: A line chart is ideal for showing continuous trends and progression over time.\n")




# ==================== Task 4 ====================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

axes[0].scatter(gap_2007["gdpPercap"], gap_2007["lifeExp"], alpha=0.7, color="purple")
axes[0].set_title("GDP per Capita vs Life Expectancy (Linear Scale)")
axes[0].set_xlabel("GDP per Capita ($)")
axes[0].set_ylabel("Life Expectancy (Years)")
axes[0].grid(True)

axes[1].scatter(gap_2007["gdpPercap"], gap_2007["lifeExp"], alpha=0.7, color="green")
axes[1].set_title("GDP per Capita vs Life Expectancy (Log Scale)")
axes[1].set_xlabel("GDP per Capita ($ - Log Scale)")
axes[1].set_ylabel("Life Expectancy (Years)")
axes[1].set_xscale("log")
axes[1].grid(True)

plt.tight_layout()
plt.show()

print("The right chart (log scale) is much easier to read because income data is heavily skewed; the log scale spreads out lower-income countries evenly, revealing a clear logarithmic curve relationship.\n")




# ==================== Task 5 ====================
fig5 = px.scatter(
    gap_2007, x="gdpPercap", y="lifeExp", size="pop", color="continent",
    hover_name="country", log_x=True, size_max=50, title="Gapminder Bubble Chart (2007)"
)
fig5.show()

print("Continent with most countries with low life expectancy: Africa.")
print("Largest bubbles: China and India.\n")



# ==================== Task 6 ====================
corr_matrix = gap_2007[["lifeExp", "pop", "gdpPercap"]].corr()
print(corr_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()

print("Most strongly related pair: lifeExp and gdpPercap (strong positive correlation).")
print("Almost no relationship pair: pop and gdpPercap (correlation close to zero).\n")



# ==================== Task 7 ====================
pivot = gap.pivot_table(index="continent", columns="year", values="lifeExp", aggfunc="mean")
print(pivot)

plt.figure(figsize=(10, 6))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Average Life Expectancy by Continent Over Time")
plt.xlabel("Year")
plt.ylabel("Continent")
plt.show()

print("Continent with lowest values throughout: Africa.")
print("Years where color changes fastest: Between 1950s and 1970s (showing rapid global health improvements).\n")




# ==================== Task 8 ====================
task8_table = pd.DataFrame({
    "Situation": [
        "Compare the number of students in five branches",
        "Show how a city's temperature changed month by month in a year",
        "Check whether more study hours go with higher marks",
        "Show how the marks of 100 students are spread out",
        "Show attendance of 5 subjects over 6 weeks in one view"
    ],
    "Best Chart": ["Bar", "Line", "Scatter", "Histogram", "Heatmap"],
    "Reason": [
        "Best for comparing discrete categories.",
        "Ideal for showing trends and changes continuously over time.",
        "Perfect for identifying relationships between two numerical variables.",
        "Great for displaying the distribution and frequency of a single variable.",
        "Excellent for spotting patterns and values across a two-dimensional grid."
    ]
})
print(task8_table.to_markdown(index=False))
print("\n")




# ==================== Task 9 ====================

bad = gap_2007[gap_2007["continent"] == "Europe"].nlargest(8, "lifeExp")
plt.figure(figsize=(6, 4))
plt.bar(bad["country"], bad["lifeExp"], color=["red", "green", "blue", "yellow", "pink", "orange", "purple", "black"])
plt.ylim(79, 82)
plt.title("Poorly Designed Chart Example")
plt.show()


plt.figure(figsize=(10, 5))
plt.bar(bad["country"], bad["lifeExp"], color="steelblue", edgecolor="black")
plt.ylim(0, 90)  # Starts at 0
plt.title("Top 8 European Countries by Life Expectancy (2007)", fontsize=12)
plt.xlabel("Country", fontsize=10)
plt.ylabel("Life Expectancy (Years)", fontsize=10)
plt.xticks(rotation=30, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

print("After fixing the y-axis to start at 0 and using a single cohesive color, the differences in life expectancy look much smaller and more realistic, avoiding visual distortion.")


# ==================== Task 10: Line Chart (Matplotlib) ====================



# ==================== Task 11: Line Chart (Matplotlib) ====================



# ==================== Task 12: Line Chart (Matplotlib) ====================






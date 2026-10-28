import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

np.random.seed(42)

df=pd.DataFrame({
    "Month":["Jan","Feb",'Mar','Arp','May','June','July','Aug','Sept','Oct','Nov','Dec'],
    'North':[120,230,239,102,273,123,384,456,324,546,223,234],
    'South':[121,232,233,1034,243,125,354,455,326,566,263,264],
    'East':[170,270,279,107,237,127,387,457,327,576,226,236],
    'West':[127,235,259,502,543,523,584,557,524,545,523,634],
    'Marketing_Spend':[12,20,59,52,53,13,38,45,32,54,23,24],
    'Customers':[420,430,249,142,443,124,344,445,424,544,423,243],
})

df["Total_Sales"]=df[['North','South','East','West']].sum(axis=1)
df['Profit']=(df['Total_Sales']*.2).round(2)

print(df)

sales_data=df.groupby("Month")["Total_Sales"].agg({"sum","mean"})
print(sales_data)

regions=['North', 'South', 'East','West']
sales=[120,100,80,90]           #in thousands
plt.figure(figsize=(9,5))
plt.bar(regions,sales,color='steelblue')
plt.title('Regional Sales Comparison')
plt.xlabel('Region')
plt.ylabel('Sales (₹ thousands)')
plt.grid(axis='y',alpha=0.3)
plt.show()

jan=[120,100,80,90]
feb=[130,110,70,75]
mar=[180,122,50,60]
x=np.arange(len(regions))
width=0.35
plt.figure(figsize=(10,5))
plt.bar(x-width/2,jan, width=width,label="Jan")
plt.bar(x-width/6,feb, width=width,label="Feb")
plt.bar(x-width/12,feb, width=width,label="Mar")
plt.xticks(x,regions)
plt.xlabel('Region')
plt.ylabel('Sales (₹ thousands)')
plt.title('Jan vs Feb vs Mar Sales')
plt.grid(axis='y',alpha=0.3)
plt.legend()
plt.show()

plt.figure(figsize=(9,5))
plt.bar(regions,jan,label='Jan')
plt.bar(regions,feb,bottom='jan',label='Feb')
plt.title('Combined Sales by Region')
plt.ylabel('Sales (₹ thousands)')
plt.grid(axis='y',alpha=0.3)
plt.legend()
plt.show()

plt.figure(figsize=(12,5))
plt.plot(jan, feb, marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Trend')
plt.xlabel('Regions')
plt.ylabel('Sales (₹ thousands)')
plt.grid(True)
plt.show()

plt.figure(figsize=(11,6))
for region in ['North','South','East','West']:
    plt.plot(df['Month'],df[region], marker='o', linestyle='-', color='b',label=region)
plt.title('Regional Sales Performance')
plt.xlabel('Month')
plt.ylabel('Sales (₹ thousands)')
plt.legend()
plt.grid(True)
plt.show()

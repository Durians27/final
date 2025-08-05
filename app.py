import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Tiêu đề ứng dụng
st.title("ABC Manufacturing – Retail Sales Analysis & Forecasting")

# Biểu đồ 1: Distribution of Monthly Sales
st.header("Distribution of Monthly Sales")
sales_data = np.concatenate([np.random.normal(16000, 1000, 1000), np.random.normal(14000, 500, 500)])
fig1, ax1 = plt.subplots()
ax1.hist(sales_data, bins=30, density=True, alpha=0.6, color='purple')
mu, sigma = norm.fit(sales_data)
x = np.linspace(min(sales_data), max(sales_data), 100)
p = norm.pdf(x, mu, sigma)
ax1.plot(x, p, 'b-', lw=2)
ax1.set_title('Distribution of Monthly Sales')
ax1.set_xlabel('Sales')
ax1.set_ylabel('Frequency')
st.pyplot(fig1)

# Biểu đồ 2: Monthly Profit Trend
st.header("Monthly Profit Trend")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
profits = [2000, 2450, 2650, 3000, 2800, 3100, 3300, 3400]
fig2, ax2 = plt.subplots()
ax2.plot(months, profits, marker='o', color='green', linewidth=2)
ax2.set_title('Monthly Profit Trend')
ax2.set_xlabel('Month')
ax2.set_ylabel('Profit')
st.pyplot(fig2)

# Biểu đồ 3: Distribution of Returns
st.header("Distribution of Returns")
returns_data = np.concatenate([np.random.normal(460, 20, 1000)])
fig3, ax3 = plt.subplots()
ax3.hist(returns_data, bins=30, density=True, alpha=0.6, color='salmon')
mu, sigma = norm.fit(returns_data)
x = np.linspace(min(returns_data), max(returns_data), 100)
p = norm.pdf(x, mu, sigma)
ax3.plot(x, p, 'r-', lw=2)
ax3.set_title('Distribution of Returns')
ax3.set_xlabel('Returned Items')
ax3.set_ylabel('Frequency')
st.pyplot(fig3)

# Biểu đồ 4: Sales by Product Category
st.header("Sales by Product Category")
categories = ['Electronics', 'Furniture', 'Clothing', 'Food']
sales = [8000, 7000, 6000, 4000]
fig4, ax4 = plt.subplots()
ax4.bar(categories, sales, color=['teal', 'coral', 'slateblue', 'plum'])
ax4.set_title('Sales by Product Category')
ax4.set_xlabel('Category')
ax4.set_ylabel('Sales')
st.pyplot(fig4)

# Biểu đồ 5: Sales by Region
st.header("Sales by Region")
regions = ['North', 'South', 'East', 'West']
sales = [8000, 6500, 5000, 7500]
fig5, ax5 = plt.subplots()
ax5.bar(regions, sales, color=['teal', 'lightyellow', 'thistle', 'salmon'])
ax5.set_title('Sales by Region')
ax5.set_xlabel('Region')
ax5.set_ylabel('Sales')
st.pyplot(fig5)
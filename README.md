# CodeAlpha_Project_Data-Visualization

🎯 Objective
The goal of this project is to design and build an interactive and visually rich sales dashboard using Python's Plotly Dash library. The dashboard enables users to:

Explore sales and profit metrics across time, products, and regions.

Identify key patterns and business insights from the dataset.

Filter and visualize data dynamically based on user input.

This project is part of a data analysis and visualization practice module to showcase data storytelling and front-end dashboard design skills.

🧾 Overview
This dashboard is built using a real-world-like sales dataset and provides multiple business insights through interactive charts. It allows users to:

Visualize monthly sales trends to identify seasonal patterns.

Compare sales by product or category to evaluate performance.

Analyze regional sales distribution with pie and bar charts.

Examine sales vs. profit relationships through scatter plots.

Filter data by year, region, or product type to focus analysis.

The dashboard is implemented in Dash, an open-source Python framework for building data applications. The final product is suitable for business analysts, managers, or students interested in data visualization and decision-making tools.

📈 Visualizations Included
Sales Over Time (Line Chart)
Shows how sales vary month by month, providing seasonal or growth insights.

Sales by Product (Bar Chart)
Highlights top-performing products or categories based on total sales.

Sales by Region (Pie/Donut Chart)
Visual breakdown of regional sales distribution.

Profit vs Sales (Scatter Plot)
Reveals the relationship between sales and profit for individual products or orders.

Filter Panel
Users can filter the data by year, region, or category to drill into specific trends.

🔍 Insights Provided
Identify top-selling products and most profitable regions.

Detect underperforming areas where sales are low or unprofitable.

Analyze seasonal patterns or monthly fluctuations.

Compare sales distribution across different product categories.

🛠️ How to Run the Dashboard
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/sales-dashboard.git
cd sales-dashboard
Install Required Libraries
Make sure you're in a virtual environment and then install:

bash
Copy
Edit
pip install -r requirements.txt
Run the App

bash
Copy
Edit
python app.py
View the Dashboard
Open your browser and go to http://127.0.0.1:8050/

📁 Files Included
app.py – The main dashboard script

data.csv – The dataset used (e.g., global_superstore)

README.md – Project description and instructions

requirements.txt – List of Python packages

🔍 What the Dataset is About
The dataset used in this dashboard project is a global retail sales dataset, often referred to as Global Superstore. It contains transactional sales data, including details such as:

Order dates, product names, and sub-categories

Sales and profit values

Customer information and geographic regions

Ship modes and categories

This dataset is commonly used for sales analytics and performance tracking in business intelligence.

📊 Key Findings from the Analysis
Top Performing Products: Certain product categories such as Chairs and Phones generate significantly higher sales.

Profitability Insights: Not all high-sales products are profitable; some items (like Tables) show high sales volume but negative profit margins.

Seasonal Trends: Monthly sales analysis reveals clear peaks during the fourth quarter, possibly due to holiday promotions or end-of-year spending.

Interesting Patterns and Anomalies
Negative Profits: Several orders yield negative profits, suggesting over-discounting or high shipping costs.

Regional Disparities: While sales are relatively balanced across regions, profit margins vary significantly. Some regions generate revenue but with minimal or negative profit.

Shipping Mode Trends: A noticeable portion of high-profit orders use First Class or Same Day shipping, which might reflect priority sales or premium customer segments.

[Screencast from 2025-04-30 21-41-41.webm](https://github.com/user-attachments/assets/e7451a03-61cd-4e37-aadc-ed22c4bb9471)

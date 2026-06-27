

 SaaS Financial Performance Analysis (Python, SQL, yFinance)

This project analyzes publicly available SaaS company financial data to evaluate performance trends, profitability, and sector-level differences using Python-based data analysis techniques.

🛠 Tools & Technologies
Python (Pandas, NumPy)
SQL (DuckDB / SQLite)
yFinance API
Jupyter Notebook / Google Colab
🔄 Data Pipeline & Methodology
Extracted quarterly financial statements for selected SaaS companies using the yfinance API
Built structured time-series datasets from raw financial data
Performed data cleaning including handling missing values and inconsistent financial fields
Created engineered metrics to support analysis:
Revenue Growth (QoQ)
Revenue Delta
Net Income trends
Operating performance indicators
Designed a structured company metadata dataset including sector and country information
Merged financial datasets with company metadata using relational join operations (Pandas merge)
Conducted exploratory data analysis (EDA) to identify performance patterns across companies and sectors
Aggregated results using SQL-style groupby operations for comparative analysis
📊 Key Insights
Revenue growth patterns vary significantly across SaaS companies despite being in the same sector
Certain companies demonstrate higher operational efficiency based on consistent revenue growth trends
Sector-level aggregation highlights differences in scalability and profitability
Integration of financial and metadata sources enabled multi-dimensional performance analysis
📁 Data Source

Financial data was retrieved using the yFinance Python library, which provides access to Yahoo Finance API for publicly listed companies. The dataset is dynamically generated from live market data.

⚠️ Disclaimer

This project is for educational and analytical purposes only and does not constitute financial advice

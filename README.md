
# SaaS Financial Performance Analysis
                                                                             






                                  

 
## Project Overview

This project analyzes the quarterly financial performance of selected SaaS and technology companies using publicly available financial data retrieved through the **yfinance** Python library.

The project demonstrates an end-to-end data analytics workflow, including data collection, data cleaning, feature engineering, SQL analysis, data enrichment through joins, KPI development, and interactive dashboard creation.

The objective is to transform raw financial statements into meaningful business insights that support data-driven decision-making.

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- SQL (DuckDB)
- Plotly
- yfinance API
- Google Colab

---

## Data Pipeline & Methodology

### Data Collection

- Retrieved quarterly financial statements from the **yfinance** API.
- Collected financial metrics including Revenue, Net Income, and Operating Income.

### Data Cleaning

- Removed inconsistencies in financial columns.
- Standardized data formats.
- Identified and analyzed missing values from the source API.
- Prepared structured time-series datasets for analysis.

### Feature Engineering

Created analytical metrics including:

- Revenue Growth (Quarter-over-Quarter)
- Revenue Difference
- Growth Momentum
- Profit Efficiency
- SaaS Score (engineered composite performance metric)

### Data Enrichment

Created a structured company metadata table containing:

- Company
- Country
- Sector

Merged financial data with company metadata using **Pandas merge()**, enabling company-level, country-level, and sector-level analysis.

### SQL Analysis

Performed SQL analysis using DuckDB, including:

- GROUP BY
- HAVING
- ORDER BY
- Common Table Expressions (CTEs)
- Window Functions (ROW_NUMBER)
- INNER JOIN
- LEFT JOIN
- Aggregate Functions (AVG, MAX)

### Interactive Dashboard

Developed an interactive dashboard in Google Colab using Plotly.

Dashboard features include:

- Company filter
- Revenue trend visualization
- Moving Average trend smoothing
- KPI summary
- Company-level financial analysis

---

## Key Performance Indicators (KPIs)

The following KPIs were analyzed or engineered during the project:

- Revenue
- Revenue Growth
- Net Income
- Operating Income
- Growth Momentum
- Profit Efficiency
- SaaS Score

---

## Dashboard Preview


---

## Business Insights

- Microsoft (MSFT) recorded the highest average quarterly revenue among the analyzed companies, reflecting its significantly larger business scale.

- Shopify showed the highest average quarterly revenue growth, indicating a faster growth trajectory despite having a smaller revenue base.

- Microsoft also generated the highest net income, demonstrating strong profitability alongside revenue leadership.

- Revenue growth patterns differed across companies, highlighting differences in business maturity and growth strategies.

- Merging financial data with company metadata enabled additional analysis across countries and business sectors.

- The engineered **Growth Momentum** and **SaaS Score** metrics provided a broader perspective by combining growth and profitability into comparable performance indicators.

- Applying a 3-period moving average reduced short-term fluctuations and improved the interpretation of long-term revenue trends.

---

## SQL Example

```sql
SELECT
    Company,
    AVG(Revenue) AS Avg_Revenue
FROM saas
GROUP BY Company
ORDER BY Avg_Revenue DESC;
```

Example Result

| Company | Average Revenue |
|---------|----------------:|
| MSFT | 77.67B |
| CRM | 10.53B |
| ADBE | 6.21B |
| SHOP | 2.95B |
| HUBS | 0.80B |

---

## Data Source

Financial data was collected using the **yfinance** Python library, which retrieves publicly available financial information from Yahoo Finance.

Company metadata (Country and Sector) was created manually to enrich the financial dataset for analytical purposes.

---

## Disclaimer

This project was created for educational and portfolio purposes only.

The engineered KPIs (Growth Momentum, Profit Efficiency, and SaaS Score) were developed to demonstrate feature engineering and comparative financial analysis. They should not be interpreted as official financial or investment metrics.

This project does not constitute financial or investment advice.

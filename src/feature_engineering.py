summary = con.execute("""
SELECT
    Company,
    AVG(Revenue) AS avg_revenue,
    AVG(Revenue_Growth) AS avg_growth,
    AVG(Magic_Number) AS avg_magic_number,
    AVG(NetIncome) AS avg_net_income
FROM saas
GROUP BY Company
""").df()

summary

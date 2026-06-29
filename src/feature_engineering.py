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

Company	avg_revenue	avg_growth	avg_magic_number	avg_net_income
0	CRM	1.053160e+10	0.032351	NaN	1.912800e+09
1	ADBE	6.214200e+09	0.030326	inf	1.784000e+09
2	MSFT	7.766780e+10	0.043324	inf	3.020800e+10
3	SHOP	2.945200e+09	0.087804	NaN	1.300000e+08
4	HUBS	8.024524e+08	0.053953	inf	1.569300e+07

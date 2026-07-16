CREATE DATABASE earnings_drift;

USE earnings_drift;

CREATE TABLE stock_prices (
	ticker VARCHAR(10),
    date DATE,
    close FLOAT 
);

CREATE TABLE earnings_dates (
	ticker VARCHAR(10),
    earnings_date DATE,
    eps_estimate FLOAT,
    reported_eps FLOAT,
    surprise_pct FLOAT 
);

SELECT
	ticker,
    earnings_date,
    close_before,
    close_after,
    ROUND(((close_after - close_before) / close_before) * 100, 2) AS pct_change
FROM (
	SELECT 
		e.ticker,
		e.earnings_date,
		(SELECT sp1.close 
		 FROM stock_prices AS sp1
		 WHERE sp1.ticker = e.ticker
		 AND sp1.date <= DATE_SUB(e.earnings_date, INTERVAL 3 DAY)
		 ORDER BY sp1.date DESC
		 LIMIT 1) AS close_before,
		(SELECT sp2.close
		 FROM stock_prices AS sp2
		 WHERE sp2.ticker = e.ticker
		 AND sp2.date >= DATE_ADD(e.earnings_date, INTERVAL 3 DAY)
		 ORDER BY sp2.date
		 LIMIT 1) AS close_after
	FROM earnings_dates AS e
) AS results
WHERE close_before IS NOT NULL
AND close_after IS NOT NULL;
	

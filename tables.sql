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
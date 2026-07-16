import pandas as pd
from sqlalchemy import text
from data_collection import get_tickers
from database import engine

with engine.connect() as conn:
    conn.execute(text('TRUNCATE TABLE stock_prices'))
    conn.execute(text('TRUNCATE TABLE earnings_dates'))
    conn.commit()

tickers = get_tickers()
for ticker in tickers:
    df_price = pd.read_csv(f'{ticker}_prices.csv')
    df_price['Ticker'] = ticker
    df_price.to_sql('stock_prices', con=engine, if_exists='append', index = False)

    df_earnings = pd.read_csv(f'{ticker}_earnings.csv')
    df_earnings.rename(columns = {
        'Earnings Date': 'earnings_date',
        'EPS Estimate': 'eps_estimate',
        'Reported EPS': 'reported_eps',
        'Surprise(%)': 'surprise_pct'
    }, inplace = True)
    df_earnings['Ticker'] = ticker
    df_earnings.to_sql('earnings_dates', con=engine, if_exists='append', index = False)
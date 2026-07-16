import yfinance as yf

def get_tickers():
    tickers = []

    user_ticker = input('Enter Ticker Here (Press "Q" to Exit)')
    while user_ticker.strip().lower() != 'q':
        tickers.append(user_ticker.strip().upper())
        user_ticker = input('Enter Ticker Here (Press "Q" to Exit)')
    
    for ticker in tickers:
        stock = yf.Ticker(ticker)

        hist = stock.history(start = '2023-06-25', end = '2025-06-25')
        hist.reset_index(inplace = True)
        hist = hist[['Date', 'Close']]
        hist.to_csv(f'{ticker}_prices.csv', index = False)
        print(f'Saved {ticker}_prices.csv')

        earnings = stock.get_earnings_dates()
        earnings.reset_index(inplace = True)
        earnings.to_csv(f'{ticker}_earnings.csv', index = False)
        print(f'Saved {ticker}_earnings.csv')
    
    return tickers

if __name__ == '__main__':
    get_tickers()
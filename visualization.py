import matplotlib.pyplot as plt
from analysis import query_df

tickers = query_df['ticker'].dropna().unique()

for ticker in tickers:
    df_ticker = query_df[query_df['ticker'] == ticker].sort_values('earnings_date')

    plt.figure(figsize = (8, 4))

    for index, row in df_ticker.iterrows():
        plt.plot([0, 1], [row['close_before'], row['close_after']], marker = 'o')
        plt.text(0, row['close_before'], f'${row["close_before"]:.2f}', va = 'center', ha = 'right', fontsize = 8)
        plt.text(1, row['close_after'], f'${row["close_after"]:.2f}', va = 'center', ha = 'left', fontsize = 8)

    plt.xticks([0, 1], ['Before Release of Earnings', 'After Release of Earnings'])
    plt.title(f'{ticker} Earnings Drift (Price Change Before and After Earnings)')
    plt.ylabel('Stock Price ($)')
    plt.grid(True, axis = 'y', linestyle = '--', alpha = 0.6)
    plt.tight_layout()

plt.show()
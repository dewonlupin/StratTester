import yfinance as yf
import os
import pandas as pd
import warnings

API_KEY = '0JTFWBJNMTNXPYEX'
# Ignore specific FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)


class StockDataDownloader:
    def __init__(self, stock_name, start_date, end_date, base_path='../../data/processed/'):
        self.stock_name = stock_name
        self.start_date = start_date
        self.end_date = end_date
        self.base_path = base_path

    def download_stock_data(self):
        stock = yf.Ticker(self.stock_name)
        data = stock.history(start=self.start_date, end=self.end_date)

        # Check if the 'Dividends' column exists and if not, add it.
        if 'Dividends' not in data.columns:
            data['Dividends'] = 0.0

        # Selecting 'Close' and 'Dividends' columns
        data_final = data[['Close', 'Dividends']].copy()
        return data_final

    def save_to_csv(self, data):
        filename = f"{self.stock_name}_DAILY.csv"
        filepath = os.path.join(self.base_path, filename)
        data.to_csv(filepath)
        print(f"Data saved to {filepath}")

    def run(self):
        # Download stock data
        data = self.download_stock_data()

        # Save data to CSV
        self.save_to_csv(data)


# Usage
if __name__ == "__main__":
    stock_name = input("Stock Name: ")
    start_date = input("Starting Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    downloader = StockDataDownloader(stock_name, start_date, end_date)
    downloader.run()

    '''
EARN
2022-01-03
2024-01-03
    '''
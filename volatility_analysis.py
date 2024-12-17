import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def calculate_volatility(dataframe, period='daily'):
    """
    Calculate daily or monthly volatility.
    
    Args:
        dataframe (pd.DataFrame): The dataframe containing cryptocurrency price data.
        period (str): 'daily' or 'monthly' for volatility calculation.
    
    Returns:
        float: Calculated volatility.
    """
    if period == 'daily':
        returns = dataframe['Close'].pct_change()
    elif period == 'monthly':
        # Ensure the 'Date' column is the index or resample won't work
        if not isinstance(dataframe.index, pd.DatetimeIndex):
            dataframe = dataframe.set_index('Date')
        returns = dataframe['Close'].resample('ME').ffill().pct_change()  # Updated 'M' to 'ME'
    else:
        raise ValueError("Period must be 'daily' or 'monthly'.")
    
    # Remove NaN values before calculating std
    return returns.dropna().std()

def plot_volatility(dataframe, ticker):
    """
    Plot the rolling volatility of the cryptocurrency.
    
    Args:
        dataframe (pd.DataFrame): The dataframe containing cryptocurrency price data.
        ticker (str): The cryptocurrency ticker for labeling the plot.
    """
    returns = dataframe['Close'].pct_change()
    rolling_volatility = returns.rolling(window=20).std()

    # Ensure rolling_volatility doesn't contain NaN values before plotting
    rolling_volatility = rolling_volatility.dropna()
    
    plt.figure(figsize=(10, 5))
    plt.plot(rolling_volatility, label="Rolling Volatility")
    plt.title(f"{ticker} Rolling Volatility (20-Day Window)")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
if __name__ == "__main__":
    ticker = "BTC-USD"  # Example ticker
    start_date = "2023-01-01"
    end_date = "2023-12-01"

    try:
        # Fetch data using yfinance
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        
        if data.empty:
            print(f"No data available for {ticker}. Please check the ticker or date range.")
        else:
            # Calculate daily and monthly volatility
            daily_volatility = calculate_volatility(data, period='daily')
            monthly_volatility = calculate_volatility(data, period='monthly')

            print(f"Daily Volatility for {ticker}: {daily_volatility}")
            print(f"Monthly Volatility for {ticker}: {monthly_volatility}")

            # Plot the rolling volatility
            plot_volatility(data, ticker)
    except Exception as e:
        print(f"An error occurred: {e}")

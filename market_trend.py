import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Define the functions directly in the file
def get_historical_data(ticker, start_date, end_date):
    #Fetch historical price data for a cryptocurrency.
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        raise ValueError(f"Error fetching data: {e}")

def plot_price_trends(dataframe, ticker):
    """Plot the historical closing price trend."""
    if 'Close' not in dataframe:
        raise ValueError("Dataframe does not contain 'Close' prices.")
    dataframe['Close'].plot(title=f"{ticker} Closing Price Trend", figsize=(10, 5))
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.show()

def analyze_csv_file(file_path):
    #Load, preprocess, and analyze a CSV file.
    try:
        # Load the dataset
        data = pd.read_csv(file_path)
        print(f"CSV file '{file_path}' loaded successfully!")
        print("Data preview:")
        print(data.head())
        
        # Check the dataset's basic info
        print(f"Dataset has {data.shape[0]} rows and {data.shape[1]} columns.")
        print("Missing values per column:")
        print(data.isnull().sum())
        
        # Drop rows with missing values
        data = data.dropna()
        print(f"Dataset shape after dropping missing values: {data.shape}")
        
        # Convert 'Date' column to datetime
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'])
        else:
            raise ValueError("The dataset does not have a 'Date' column.")
        
        # Perform analysis: Plot Closing Prices
        if 'Close' in data.columns:
            plt.figure(figsize=(10, 6))
            plt.plot(data['Date'], data['Close'], marker='o', label='Closing Price')
            plt.title('Closing Price Trend')
            plt.xlabel('Date')
            plt.ylabel('Closing Price')
            plt.grid()
            plt.legend()
            plt.show()
        else:
            raise ValueError("The dataset does not have a 'Close' column.")
        
        # Additional visualizations or analysis
        if 'Volume' in data.columns:
            plt.figure(figsize=(10, 6))
            plt.bar(data['Date'], data['Volume'], color='orange', label='Volume')
            plt.title('Trading Volume Over Time')
            plt.xlabel('Date')
            plt.ylabel('Volume')
            plt.grid()
            plt.legend()
            plt.show()
        
        print("CSV file analysis completed successfully!")
    
    except Exception as e:
        print(f"An error occurred while analyzing the CSV file: {e}")
        
def calculate_macd(dataframe, ticker, short_window=12, long_window=26, signal_window=9):
    #Calculate and plot the MACD (Moving Average Convergence Divergence) indicator.
    if 'Close' not in dataframe:
        raise ValueError("Dataframe does not contain 'Close' prices.")

    # Calculate EMAs
    short_ema = dataframe['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = dataframe['Close'].ewm(span=long_window, adjust=False).mean()

    # Calculate MACD and Signal Line
    dataframe['MACD'] = short_ema - long_ema
    dataframe['Signal Line'] = dataframe['MACD'].ewm(span=signal_window, adjust=False).mean()

    # Plot MACD
    plt.figure(figsize=(10, 6))
    plt.plot(dataframe.index, dataframe['MACD'], label='MACD', color='blue')
    plt.plot(dataframe.index, dataframe['Signal Line'], label='Signal Line', color='red')
    plt.bar(dataframe.index, dataframe['MACD'] - dataframe['Signal Line'], color='gray', alpha=0.3, label='MACD Histogram')
    plt.title(f'{ticker} MACD Indicator')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    print("Running market_trend.py...")  # Debugging print

    # Example parameters for cryptocurrency data
    ticker = "BTC-USD"
    start_date = "2023-01-01"
    end_date = "2023-12-01"

    # Fetch historical data
    try:
        print(f"Fetching data for {ticker} from {start_date} to {end_date}...")
        data = get_historical_data(ticker, start_date, end_date)
        if data is not None and not data.empty:
            print("Data fetched successfully:")
            print(data.head())  # Print the first few rows of data
            
            # Plot price trends
            print("Plotting data...")
            plot_price_trends(data, ticker)
        else:
            print(f"No data returned for {ticker}.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Specify the path to your CSV file
    csv_file_path = '~/Documents/crypto_analysis_toolkit/data/sample_data.csv'
    
    # Analyze the CSV file
    analyze_csv_file(csv_file_path)

    # Calculate and plot MACD
    print("Calculating and plotting MACD...\n")
    data1 = get_historical_data(ticker, start_date, end_date)
    calculate_macd(data1, ticker)

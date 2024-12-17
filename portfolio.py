import pandas as pd
import numpy as np
import yfinance as yf

def add_to_portfolio(portfolio, ticker, quantity):
 #Add a cryptocurrency or stock to the portfolio.
    
    if ticker in portfolio:
        portfolio[ticker] += quantity
    else:
        portfolio[ticker] = quantity
    return portfolio

def calculate_portfolio_returns(portfolio, start_date, end_date):

    #Calculate the portfolio's total return over a specified period.
    total_return = 0
    for ticker, quantity in portfolio.items():
        try:
            # Download historical data for the ticker
            data = yf.download(ticker, start=start_date, end=end_date, progress=False)
            if data.empty:
                print(f"No data found for {ticker}. Skipping.")
                continue
            
            # Calculate daily returns
            data['Daily Return'] = data['Close'].pct_change()
            
            # Compute the average return and multiply by quantity
            average_daily_return = data['Daily Return'].mean()
            total_return += average_daily_return * quantity
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    
    return total_return * 100  # Return as a percentage

# Example usage
if __name__ == "__main__":
    # Define a portfolio
    portfolio = {}
    portfolio = add_to_portfolio(portfolio, "BTC-USD", 2)
    portfolio = add_to_portfolio(portfolio, "ETH-USD", 5)
    
    # Calculate portfolio returns
    start_date = "2023-01-01"
    end_date = "2023-12-01"
    total_returns = calculate_portfolio_returns(portfolio, start_date, end_date)
    
    print(f"Total portfolio return from {start_date} to {end_date}: {total_returns:.2f}%")

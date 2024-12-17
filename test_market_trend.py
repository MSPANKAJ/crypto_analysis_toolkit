import pytest
import os
import pandas as pd
from crypto_analysis_toolkit.market_trend import (
    get_historical_data,
    plot_price_trends,
    analyze_csv_file,
)

def test_get_historical_data():
    """Test the get_historical_data function for valid output."""
    data = get_historical_data("BTC-USD", "2023-01-01", "2023-12-01")
    assert not data.empty, "Historical data should not be empty."
    assert "Close" in data.columns, "The data should contain a 'Close' column."

def test_plot_price_trends():
    """Test the plot_price_trends function."""
    data = get_historical_data("BTC-USD", "2023-01-01", "2023-12-01")
    try:
        plot_price_trends(data, "BTC-USD")
    except Exception as e:
        pytest.fail(f"Plotting failed with error: {e}")

def test_analyze_csv_file(tmp_path):
    """Test the analyze_csv_file function with a sample CSV."""
    # Create a temporary sample CSV file
    sample_csv_path = tmp_path / "sample_data.csv"
    sample_data = {
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "Open": [16500, 16700, 16950],
        "High": [16800, 17000, 17100],
        "Low": [16450, 16600, 16800],
        "Close": [16700, 16950, 17050],
        "Volume": [120000, 130000, 140000],
        "Adj Close": [16700, 16950, 17050],
    }
    sample_df = pd.DataFrame(sample_data)
    sample_df.to_csv(sample_csv_path, index=False)

    # Run the analyze_csv_file function
    try:
        analyze_csv_file(str(sample_csv_path))
    except Exception as e:
        pytest.fail(f"Analyzing CSV file failed with error: {e}")

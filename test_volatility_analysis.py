import pytest
import pandas as pd
import numpy as np  # Add necessary imports
from crypto_analysis_toolkit.volatility_analysis import calculate_volatility

def test_calculate_daily_volatility():
    # Create a mock DataFrame
    data = pd.DataFrame({
        'Date': pd.date_range(start="2023-01-01", periods=5, freq='D'),
        'Close': [100, 102, 101, 104, 103]
    })
    # Test daily volatility
    daily_volatility = calculate_volatility(data, period='daily')
    assert isinstance(daily_volatility, float)

def test_calculate_monthly_volatility():
    # Create a mock DataFrame
    data = pd.DataFrame({
        'Date': pd.date_range(start="2023-01-01", periods=30, freq='D'),
        'Close': np.random.randint(100, 200, 30)
    })
    # Test monthly volatility
    monthly_volatility = calculate_volatility(data, period='monthly')
    assert isinstance(monthly_volatility, float)

def test_invalid_period():
    # Create a mock DataFrame
    data = pd.DataFrame({
        'Date': pd.date_range(start="2023-01-01", periods=5, freq='D'),
        'Close': [100, 102, 101, 104, 103]
    })
    # Test invalid period
    with pytest.raises(ValueError):
        calculate_volatility(data, period='yearly')

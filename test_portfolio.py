import pytest
from crypto_analysis_toolkit.portfolio import add_to_portfolio

def test_add_to_portfolio():
    portfolio = {}
    updated_portfolio = add_to_portfolio(portfolio, "BTC-USD", 10)
    assert updated_portfolio["BTC-USD"] == 10
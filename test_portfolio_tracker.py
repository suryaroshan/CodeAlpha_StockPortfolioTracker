"""
Automated Test Suite for Stock Portfolio Tracker
------------------------------------------------
Unit tests verifying stock calculations, input validation,
portfolio summary calculations, and CSV export functionality.
"""

import csv
import io
import os
import sys
import unittest
from unittest.mock import patch

import portfolio_tracker


class TestStockPortfolioTracker(unittest.TestCase):

    def setUp(self):
        self.test_csv_file = "test_portfolio.csv"

    def tearDown(self):
        if os.path.exists(self.test_csv_file):
            try:
                os.remove(self.test_csv_file)
            except OSError:
                pass

    def test_stock_prices_dictionary(self):
        """Verify the predefined dictionary contains required stocks and prices."""
        expected_prices = {
            "AAPL": 180,
            "TSLA": 250,
            "MSFT": 300,
            "GOOGL": 150,
            "AMZN": 200,
        }
        self.assertEqual(portfolio_tracker.STOCK_PRICES, expected_prices)

    def test_calculate_total_investment(self):
        """Verify the calculation of total portfolio investment."""
        portfolio = {"AAPL": 2, "TSLA": 3}
        # (2 * 180) + (3 * 250) = 360 + 750 = 1110
        total = portfolio_tracker.calculate_total_investment(portfolio)
        self.assertEqual(total, 1110.0)

    def test_empty_portfolio_calculation(self):
        """Verify empty portfolio returns 0.0 total."""
        self.assertEqual(portfolio_tracker.calculate_total_investment({}), 0.0)

    def test_save_empty_portfolio_to_csv(self):
        """Verify saving an empty portfolio returns False and does not create file."""
        saved = portfolio_tracker.save_portfolio_to_csv({}, self.test_csv_file)
        self.assertFalse(saved)
        self.assertFalse(os.path.exists(self.test_csv_file))

    def test_save_valid_portfolio_to_csv(self):
        """Verify CSV saving writes the correct headers, stock details, and total row."""
        portfolio = {"AAPL": 5, "MSFT": 2}
        saved = portfolio_tracker.save_portfolio_to_csv(portfolio, self.test_csv_file)
        self.assertTrue(saved)
        self.assertTrue(os.path.exists(self.test_csv_file))

        # Read back CSV and verify content
        with open(self.test_csv_file, mode="r", encoding="utf-8") as f:
            reader = list(csv.reader(f))

        # Check header
        self.assertEqual(reader[0], ["Stock Symbol", "Price per Share ($)", "Quantity", "Total Investment ($)"])
        # Check AAPL row: 5 shares at $180 = $900
        self.assertEqual(reader[1], ["AAPL", "180.00", "5", "900.00"])
        # Check MSFT row: 2 shares at $300 = $600
        self.assertEqual(reader[2], ["MSFT", "300.00", "2", "600.00"])

        # Check summary row: Total $1500
        self.assertEqual(reader[4], ["OVERALL TOTAL INVESTMENT", "", "", "1500.00"])

    @patch("builtins.input", side_effect=["0", "-5", "abc", "10"])
    def test_get_valid_quantity(self, mock_input):
        """Verify invalid inputs (zero, negative, text) are rejected until valid number is provided."""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        quantity = portfolio_tracker.get_valid_quantity()

        sys.stdout = sys.__stdout__
        self.assertEqual(quantity, 10)
        output = captured_output.getvalue()
        self.assertIn("Quantity must be greater than 0", output)
        self.assertIn("Invalid quantity", output)

    @patch("builtins.input", side_effect=["INVALID", "AAPL", "5", "n"])
    def test_add_stock_to_portfolio(self, mock_input):
        """Verify invalid symbols prompt error, valid symbols add correctly."""
        portfolio = {}
        captured_output = io.StringIO()
        sys.stdout = captured_output

        portfolio_tracker.add_stock_to_portfolio(portfolio)

        sys.stdout = sys.__stdout__
        self.assertEqual(portfolio, {"AAPL": 5})
        output = captured_output.getvalue()
        self.assertIn("'INVALID' is not a valid stock", output)
        self.assertIn("Successfully added 5 share(s) of AAPL", output)


if __name__ == "__main__":
    unittest.main()

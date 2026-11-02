# Stock Portfolio Tracker (Python)

A beginner-friendly, console-based **Stock Portfolio Tracker** application developed in Python. Designed for tracking stock investments, calculating individual stock values, computing overall portfolio worth, and exporting financial summaries to a CSV file.

Developed for **CodeAlpha Internship** submission.

---

## 📌 Project Description

The Stock Portfolio Tracker helps users manage their stock holdings in real time. It uses a predefined dictionary of stock market prices (`AAPL`, `TSLA`, `MSFT`, `GOOGL`, and `AMZN`), allows users to add multiple stocks with custom quantities, automatically calculates investment amounts, displays clean tabular summaries, and exports data to CSV using Python's built-in `csv` module.

---

## ✨ Features

- **Hardcoded Stock Price Dictionary**: Supports real-time price lookups for 5 popular stocks:
  - `AAPL`: \$180.00
  - `TSLA`: \$250.00
  - `MSFT`: \$300.00
  - `GOOGL`: \$150.00
  - `AMZN`: \$200.00
- **View Available Stocks**: Clear tabular display of all available symbols and their corresponding prices.
- **Add Multiple Stocks**: Users can enter stock symbols and share quantities. If a stock is purchased multiple times, the portfolio automatically aggregates the total shares.
- **Robust Input Validation**:
  - Handles invalid / unrecognized stock symbols with informative guidance.
  - Rejects zero, negative, or non-numeric share quantities.
- **Investment Calculation**: Automatically computes the subtotal for each stock (`Quantity × Price`) and the overall total portfolio valuation.
- **Detailed Portfolio Summary**: Formatted tabular view showing stock symbol, unit price, quantity owned, and subtotal investment.
- **CSV Data Export**: Built-in export functionality utilizing Python's native `csv` module to save portfolio records into `portfolio.csv`.
- **User-Friendly Menu & Clean Exit**: Interactive 5-option menu system with an option to save before quitting.

---

## 📋 Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: Python 3.x
- **Dependencies**: No external libraries needed (uses only Python standard library: `csv`, `os`).

---

## 📁 Project Structure

```text
stock_portfolio_tracker/
│
├── portfolio_tracker.py       # Main application script with complete portfolio logic
├── README.md                  # Project overview, features, and run instructions
├── test_portfolio_tracker.py  # Automated unit test suite verifying calculations and CSV output
└── .gitignore                 # Excludes cache files and temporary test exports
```

---

## 🚀 How to Run the Program

### 1. Open Terminal / Command Prompt
Navigate to the project directory:

```bash
cd "C:\Users\surya roshan\.gemini\antigravity\scratch\stock_portfolio_tracker"
```

### 2. Run the Script
Run using Python:

**On Windows:**
```bash
python portfolio_tracker.py
```
*(or `python3.14 portfolio_tracker.py`)*

**On macOS / Linux:**
```bash
python3 portfolio_tracker.py
```

### 3. Run Automated Tests
```bash
python -m unittest test_portfolio_tracker.py
```

---

## 🎮 Sample Console Walkthrough

```text
=======================================================
        WELCOME TO STOCK PORTFOLIO TRACKER       
=======================================================

--- MAIN MENU ---
1. View Available Stocks & Prices
2. Add Stock to Portfolio
3. View Portfolio Summary
4. Save Portfolio to CSV
5. Exit Program

Enter your choice (1-5): 2

========================================
        AVAILABLE STOCKS & PRICES        
========================================
Stock Symbol    Price per Share ($) 
----------------------------------------
AAPL            $180.00              
TSLA            $250.00              
MSFT            $300.00              
GOOGL           $150.00              
AMZN            $200.00              
========================================

Enter stock symbol to buy (or 'BACK' to return): AAPL
Enter quantity of shares to purchase: 5

[+] Successfully added 5 share(s) of AAPL at $180.00 each.
    Subtotal for this purchase: $900.00
    Total AAPL shares in portfolio: 5

Would you like to add another stock? (y/n): n

--- MAIN MENU ---
Enter your choice (1-5): 3

=================================================================
                   PORTFOLIO SUMMARY                     
=================================================================
Stock      Price ($)    Quantity     Total Investment ($)
-----------------------------------------------------------------
AAPL       $180.00      5            $900.00             
-----------------------------------------------------------------
OVERALL TOTAL INVESTMENT:            $900.00             
=================================================================
```

---

## 📄 CSV Export Format (`portfolio.csv`)

When choosing **Option 4** or agreeing to save on exit, `portfolio.csv` is generated:

| Stock Symbol | Price per Share (\$) | Quantity | Total Investment (\$) |
| :--- | :--- | :--- | :--- |
| AAPL | 180.00 | 5 | 900.00 |
| MSFT | 300.00 | 2 | 600.00 |
| | | | |
| **OVERALL TOTAL INVESTMENT** | | | **1500.00** |

---

## 💡 Code Architecture & Concepts Used

1. **Dictionaries**: Used for fixed price catalog mapping (`STOCK_PRICES`) and storing dynamic user holdings (`portfolio`).
2. **Modular Functions**:
   - `display_available_stocks()`: Displays stock price table.
   - `get_valid_quantity()`: Validates integer inputs.
   - `add_stock_to_portfolio()`: Manages purchasing and portfolio updating.
   - `calculate_total_investment()`: Computes total portfolio value.
   - `display_portfolio_summary()`: Formats summary output.
   - `save_portfolio_to_csv()`: Handles file output via `csv.writer`.
   - `main()`: Orchestrates user interaction loop.
3. **Loops & Exception Handling**: `try-except` blocks for safe number parsing and file I/O operations.

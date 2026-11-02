"""
Stock Portfolio Tracker
-----------------------
A beginner-friendly console application developed in Python.
Allows users to view stock prices, buy shares, track overall investment value,
and export portfolio details into a CSV file.
Suitable for Python internship project submission (CodeAlpha).
"""

import csv
import os

# Predefined dictionary containing fixed stock prices as per requirements
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOGL": 150,
    "AMZN": 200,
}


def display_available_stocks():
    """Displays all available stocks and their market prices."""
    print("\n" + "=" * 40)
    print("        AVAILABLE STOCKS & PRICES        ")
    print("=" * 40)
    print(f"{'Stock Symbol':<15} {'Price per Share ($)':<20}")
    print("-" * 40)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<15} ${price:<20.2f}")
    print("=" * 40)


def get_valid_quantity():
    """Prompts the user for a valid positive integer quantity of shares."""
    while True:
        qty_input = input("Enter quantity of shares to purchase: ").strip()
        try:
            quantity = int(qty_input)
            if quantity <= 0:
                print("[!] Quantity must be greater than 0. Please enter a valid positive number.")
                continue
            return quantity
        except ValueError:
            print("[!] Invalid quantity. Please enter a whole number (e.g., 5, 10).")


def add_stock_to_portfolio(portfolio):
    """
    Prompts user for stock symbol and quantity, validates input,
    and updates the portfolio dictionary.
    """
    display_available_stocks()

    while True:
        symbol = input("\nEnter stock symbol to buy (or 'BACK' to return): ").strip().upper()

        if symbol == "BACK":
            print("Returning to main menu.")
            return

        # Validate stock symbol
        if symbol not in STOCK_PRICES:
            print(f"[!] '{symbol}' is not a valid stock. Please choose from: {', '.join(STOCK_PRICES.keys())}")
            continue

        # Get valid share quantity
        quantity = get_valid_quantity()
        price = STOCK_PRICES[symbol]
        investment_for_stock = quantity * price

        # Update portfolio (add to existing quantity if already purchased)
        current_shares = portfolio.get(symbol, 0)
        portfolio[symbol] = current_shares + quantity

        print(f"\n[+] Successfully added {quantity} share(s) of {symbol} at ${price:.2f} each.")
        print(f"    Subtotal for this purchase: ${investment_for_stock:.2f}")
        print(f"    Total {symbol} shares in portfolio: {portfolio[symbol]}")

        # Prompt if user wants to add another stock immediately
        again = input("\nWould you like to add another stock? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            break


def calculate_total_investment(portfolio):
    """Calculates and returns the overall total investment amount across all stocks."""
    total = 0.0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES.get(symbol, 0)
        total += quantity * price
    return total


def display_portfolio_summary(portfolio):
    """Displays a detailed tabular summary of the portfolio and overall investment value."""
    print("\n" + "=" * 65)
    print("                   PORTFOLIO SUMMARY                     ")
    print("=" * 65)

    if not portfolio:
        print("Your portfolio is currently empty. Buy some shares to see them here!")
        print("=" * 65)
        return

    print(f"{'Stock':<10} {'Price ($)':<12} {'Quantity':<12} {'Total Investment ($)':<20}")
    print("-" * 65)

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        subtotal = quantity * price
        print(f"{symbol:<10} ${price:<11.2f} {quantity:<12} ${subtotal:<19.2f}")

    total_value = calculate_total_investment(portfolio)
    print("-" * 65)
    print(f"{'OVERALL TOTAL INVESTMENT:':<36} ${total_value:<20.2f}")
    print("=" * 65)


def save_portfolio_to_csv(portfolio, filename="portfolio.csv"):
    """
    Saves the portfolio details (stock, price, quantity, investment value)
    and overall total to a CSV file using Python's csv module.
    """
    if not portfolio:
        print("\n[!] Portfolio is empty. Nothing to save to CSV.")
        return False

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)

            # Write header
            writer.writerow(["Stock Symbol", "Price per Share ($)", "Quantity", "Total Investment ($)"])

            # Write individual stock rows
            for symbol, quantity in portfolio.items():
                price = STOCK_PRICES[symbol]
                subtotal = quantity * price
                writer.writerow([symbol, f"{price:.2f}", quantity, f"{subtotal:.2f}"])

            # Write summary row
            total_value = calculate_total_investment(portfolio)
            writer.writerow([])
            writer.writerow(["OVERALL TOTAL INVESTMENT", "", "", f"{total_value:.2f}"])

        print(f"\n[+] Portfolio successfully saved to: {os.path.abspath(filename)}")
        return True
    except IOError as e:
        print(f"[!] Error saving portfolio to CSV: {e}")
        return False


def main():
    """Main function containing the interactive menu loop."""
    portfolio = {}

    print("=" * 55)
    print("        WELCOME TO STOCK PORTFOLIO TRACKER       ")
    print("=" * 55)

    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Available Stocks & Prices")
        print("2. Add Stock to Portfolio")
        print("3. View Portfolio Summary")
        print("4. Save Portfolio to CSV")
        print("5. Exit Program")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            display_available_stocks()
        elif choice == "2":
            add_stock_to_portfolio(portfolio)
        elif choice == "3":
            display_portfolio_summary(portfolio)
        elif choice == "4":
            save_portfolio_to_csv(portfolio)
        elif choice == "5":
            # Offer to save if portfolio has stocks before exiting
            if portfolio:
                save_prompt = input("\nWould you like to save your portfolio to CSV before exiting? (y/n): ").strip().lower()
                if save_prompt in ["y", "yes"]:
                    save_portfolio_to_csv(portfolio)

            print("\nThank you for using Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("[!] Invalid option selected. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()

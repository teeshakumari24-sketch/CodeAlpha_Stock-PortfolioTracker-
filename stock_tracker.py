stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

portfolio = {}
total = 0

print("===== Stock Portfolio Tracker =====")

while True:
    stock = input("\nEnter Stock Name (or type done): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter Quantity: "))

    portfolio[stock] = quantity

print("\n------ Portfolio Summary ------")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total += value
    print(f"{stock} : {quantity} shares × ${stock_prices[stock]} = ${value}")

print("\nTotal Investment Value = $", total)

with open("portfolio.txt", "w") as file:
    file.write("Portfolio Summary\n\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock} : {quantity} shares = ${value}\n")

    file.write(f"\nTotal Investment = ${total}")

print("\nPortfolio saved successfully in portfolio.txt")
stocks = [
    {"ticker": "AAPL", "buy": 150, "sell": 180},
    {"ticker": "TSLA", "buy": 200, "sell": 140},
    {"ticker": "MSFT", "buy": 300, "sell": 230},
    {"ticker": "NVDA", "buy": 400, "sell": 365}
]
def calculate_profit(sell, buy):
    return sell - buy

def calculate_return(sell, buy):
    return ((sell - buy) / buy) * 100

for stock in stocks:
    profit = calculate_profit(
        stock["sell"],
        stock["buy"]
    )
    returns = calculate_return(
        stock["sell"],
        stock["buy"]
    )

    if profit > 0:
        print("Profitable Trade")
    else:
        print("Loss Trade")

    print("ticker:", stock["ticker"])
    print("Profit:", profit)
    print("Return %", round(returns, 2))
    print("     ")
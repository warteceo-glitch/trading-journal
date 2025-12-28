import pandas as pd
import matplotlib.pyplot as plt

# 1?? ?????? ???? ???????
df = pd.read_csv("sample_trades.csv")

# 2?? ?????? ??? / ??? ?? ??????
def calculate_pnl(row):
    if row["Position"] == "Long":
        return (row["Exit_Price"] - row["Entry_Price"]) * row["Quantity"]
    else:
        return (row["Entry_Price"] - row["Exit_Price"]) * row["Quantity"]

df["PnL"] = df.apply(calculate_pnl, axis=1)

# 3?? ????? ??????? ??? ? ????
df["Result"] = df["PnL"].apply(lambda x: "Win" if x > 0 else "Loss")

# 4?? ?????? ???? ?????
total_trades = len(df)
wins = len(df[df["PnL"] > 0])
losses = len(df[df["PnL"] <= 0])
win_rate = round((wins / total_trades) * 100, 2)
total_profit = round(df["PnL"].sum(), 2)

# 5?? Equity Curve
df["Equity"] = df["PnL"].cumsum()

# 6?? ????? ?????
print("?? TRADING JOURNAL REPORT")
print("----------------------------")
print(f"Total Trades: {total_trades}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Win Rate: {win_rate}%")
print(f"Total PnL: {total_profit}")
print("----------------------------")

# 7?? ??? ??????
plt.figure()
plt.plot(df["Equity"])
plt.title("Equity Curve")
plt.xlabel("Trade Number")
plt.ylabel("Equity")
plt.grid(True)
plt.show()
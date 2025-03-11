import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# Pandas 是一个功能强大的开源数据处理和分析库，专门设计用于高效地进行数据分析和操作。
# yfinance 是一个用于获取金融数据的库，支持从 Yahoo Finance 获取股票、指数和其他金融市场数据。
# Matplotlib 是一个二维绘图库，用于创建静态、动态和交互式的数据可视化图表。

# pip install pandas yfinance matplotlib


# 获取股票数据
symbol = "600519.SS"
start_date = "2021-01-01"
end_date = "2025-01-01"

data = yf.download(symbol, start=start_date, end=end_date)

# 计算移动平均
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_100'] = data['Close'].rolling(window=100).mean()

# 初始化交叉信号列
data['Signal'] = 0

# 计算交叉信号
data.loc[data['SMA_20'] > data['SMA_100'], 'Signal'] = 1
data.loc[data['SMA_20'] < data['SMA_100'], 'Signal'] = -1

# 计算每日收益率
data['Daily_Return'] = data['Close'].pct_change()

# 计算策略信号的收益率（shift(1) 是为了避免未来数据的偏差）
data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']

# 计算累计收益
data['Cumulative_Return'] = (1 + data['Strategy_Return']).cumprod()

# 输出策略表现
strategy_performance = {
    'Total Return': data['Cumulative_Return'].iloc[-1] - 1,
    'Annualized Return': (data['Cumulative_Return'].iloc[-1] ** (252 / len(data))) - 1,
    'Max Drawdown': (data['Cumulative_Return'] / data['Cumulative_Return'].cummax() - 1).min(),
}

print("策略表现:")
for key, value in strategy_performance.items():
    print(f"{key}: {value:.4f}")

# 绘制累计收益曲线
plt.figure(figsize=(10, 6))
plt.plot(data['Cumulative_Return'], label='策略收益', color='b')
plt.plot(data['Close'] / data['Close'].iloc[0], label='直接持有股票', color='g')
plt.title("Cumulative Return of Strategy vs. Stock")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.show()
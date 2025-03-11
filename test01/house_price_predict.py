import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1️⃣ 读取数据
data = pd.read_csv("house_prices.csv")

# 2️⃣ 数据预览
print(data.head())

# 3️⃣ 数据可视化
plt.scatter(data["area"], data["price"])
plt.xlabel("房屋面积（平方英尺）")
plt.ylabel("房价（美元）")
plt.title("房价 vs 面积")
plt.show()

# 4️⃣ 准备训练数据
X = data[["area", "bedrooms", "bathrooms"]]  # 特征
y = data["price"]  # 目标变量

# 5️⃣ 拆分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6️⃣ 训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 7️⃣ 预测
y_pred = model.predict(X_test)

# 8️⃣ 评估模型
mae = mean_absolute_error(y_test, y_pred)
print(f"模型 MAE 误差：{mae}")

# 9️⃣ 用户输入预测房价
new_house = np.array([[2000, 3, 2]])  # 假设一套 2000 平方英尺 3 房 2 卫的房子
predicted_price = model.predict(new_house)
print(f"预测房价：${predicted_price[0]:,.2f}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

#文件路径
file_path = r'C:\Users\13774\Desktop\Big-data-master\data\cleaning_钢笔.csv'

# 读取商品数据
data = pd.read_csv(file_path)

# 提取特征和目标变量
X = data[['价格']]  # 使用价格作为特征
y = data['销量']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 建立线性回归模型
model = LinearRegression()

# 在训练集上拟合模型
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 计算模型的均方误差
mse = mean_squared_error(y_test, y_pred)
print("均方误差（MSE）:", mse)

# 输出模型的系数和截距
print("模型系数:", model.coef_)
print("模型截距:", model.intercept_)

# 建立决策树回归模型
tree_model = DecisionTreeRegressor()

# 在训练集上拟合模型
tree_model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred_tree = tree_model.predict(X_test)

# 计算决策树模型的均方误差
mse_tree = mean_squared_error(y_test, y_pred_tree)
print("决策树模型的均方误差：", mse_tree)
# 建立随机森林回归模型

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# 在训练集上拟合模型
rf_model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred_rf = rf_model.predict(X_test)

# 计算随机森林模型的均方误差
mse_rf = mean_squared_error(y_test, y_pred_rf)
print("随机森林模型的均方误差：", mse_rf)
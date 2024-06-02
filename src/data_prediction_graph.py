import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


#文件路径
file_path = r'C:\Users\13774\Desktop\Big-data-master\data\cleaning_塑料袋_.csv'

# 读取商品数据
data = pd.read_csv(file_path)

# 提取特征和目标变量
X = data[['价格']]
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

# 绘制训练数据、测试数据和模型预测结果的散点图
plt.scatter(X_train, y_train, color='blue', label='Training data')
plt.scatter(X_test, y_test, color='red', label='Testing data')
plt.plot(X_test, y_pred, color='green', linewidth=2, label='Linear Regression Model')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.title('Linear Regression Model')
plt.legend()
plt.show()

# 绘制残差图
residuals = y_test - y_pred
plt.scatter(y_pred, residuals)
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.axhline(y=0, color='r', linestyle='-')
plt.show()

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
# 绘制随机森林模型预测结果和实际结果的散点图
plt.scatter(X_test, y_test, color='red', label='Actual')
plt.scatter(X_test, y_pred_rf, color='green', label='Predicted')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.title('Random Forest Regression Model')
plt.legend()
plt.show()

# 获取随机森林模型的特征重要性
feature_importance = rf_model.feature_importances_

# 将特征重要性可视化为条形图
feature_names = X.columns
plt.bar(feature_names, feature_importance)
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.title('Feature Importance of Random Forest Model')
plt.xticks(rotation=45)
plt.show()

# 可视化单颗决策树
from sklearn.tree import export_text
tree_rules = export_text(tree_model, feature_names=list(X.columns))
print(tree_rules)

# 定义目标销量
target_sales = 1000

# 创建包含目标销量的 DataFrame
target_data = pd.DataFrame({'销量': [target_sales]})

# 使用决策树模型进行价格预测
predicted_price = tree_model.predict(target_data)

# 输出预测的价格
print("Predicted price for sales of", target_sales, "is:", predicted_price[0])
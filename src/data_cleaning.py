import pandas as pd

name="索尼a7m4"
expected_price=15000

# 读取数据
data = pd.read_csv('../data/'+name+'.csv')

# 删除包含缺失值的行
data.dropna()

# 移除重复行
data.drop_duplicates()

# 处理异常值（数据价格应该在给定值的50%-150%）
data = data[(expected_price * 0.5 < data['价格']) & (data['价格'] < expected_price * 1.5)]

# 将筛选后的数据存储到新的CSV文件中
data.to_csv('../data/cleaning_'+name+'.csv', index=False)

print("数据处理完成，符合条件的数据已保存到 'cleaning_"+name+".csv'。")

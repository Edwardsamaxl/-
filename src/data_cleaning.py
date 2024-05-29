import pandas as pd
import numpy as np
import os

def clean_data(name):
    # 读取数据
    data = pd.read_csv('../data/' + name + '.csv')

    # 删除包含缺失值的行
    data = data.dropna()

    # 移除重复行
    data = data.drop_duplicates()

    # 将价格和销量列转换为数值类型
    data['价格'] = pd.to_numeric(data['价格'], errors='coerce')
    data['销量'] = data['销量'].str.replace('人累计付款', '').astype(int)

    # 计算平均价格作为期望价格
    expected_price = data['价格'].mean()

    # 处理异常值（数据价格应该在期望价格的50%-150%范围内）
    data = data[(expected_price * 0.15 < data['价格']) & (data['价格'] < expected_price * 2.0)]

    # 将筛选后的数据存储到新的CSV文件中
    cleaned_file_path = '../data/cleaning_' + name + '.csv'
    data.to_csv(cleaned_file_path, index=False)

    print(f"数据处理完成，符合条件的数据已保存到 '{cleaned_file_path}'。")
    return cleaned_file_path, data, expected_price

# 示例使用
name = "钢笔"
cleaned_file_path, cleaned_data, expected_price = clean_data(name)

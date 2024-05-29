import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_sales_distribution(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 手动指定价格区间
    manual_price_bins = [15, 25, 30, 35, 65, 90, 110, 155, 170, 200, 500]
    manual_labels = ['16-25', '25-30', '31-35', '36-65', '66-90', '91-110', '111-155', '156-170', '171-200', '200+']

    # 将价格分入手动指定的区间
    df['Price_Range'] = pd.cut(df['价格'], bins=manual_price_bins, labels=manual_labels, include_lowest=True)

    # 汇总每个价格区间的销售量
    sales_summary = df.groupby('Price_Range', observed=False)['销量'].sum()

    # 计算总销量
    total_sales = sales_summary.sum()

    # 计算每个价格区间的销量比例
    sales_proportion = sales_summary / total_sales

    # 检查汇总结果
    print(sales_proportion)

    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
    plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

    # 绘制柱状图
    ax = sales_proportion.plot(kind='bar')
    plt.xlabel('价格区间')
    plt.ylabel('销量比例')
    plt.title('不同价格区间的销量比例')
    plt.xticks(rotation=45)
    plt.tight_layout()  # 自动调整布局

    # 在图中标注总销量
    plt.text(0.5, 0.95, f'总销量: {total_sales}', ha='center', va='center', transform=plt.gca().transAxes)

    # 在柱状图上显示数值比例
    for i, v in enumerate(sales_proportion):
        ax.text(i, v + 0.01, f'{v:.2%}', ha='center', va='bottom')

    plt.show()


# 获取当前脚本所在目录的父目录
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 构建CSV文件的相对路径
file_path = os.path.join(base_dir, 'data', 'cleaning_钢笔.csv')

# 调用绘图函数
plot_sales_distribution(file_path)

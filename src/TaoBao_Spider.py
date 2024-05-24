# 导入自动化模块
from DrissionPage import ChromiumPage
# 导入正则表达式模块
import re
# 导入json模块
import json
# 导入csv模块
import csv
# 导入时间模块
import time
# 导入os模块获取路径
import os

# 获取当前文件所在目录的父目录路径
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)

# 构建data目录的路径
data_dir = os.path.join(parent_dir, 'data')

# 如果data目录不存在，则创建它
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# 生成csv文件的路径
csv_file_path = os.path.join(data_dir, '索尼a7m4.csv')

# 创建文件对象
f = open(csv_file_path, mode='w', encoding='utf-8', newline='')

# 字典写入方法
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '价格',
    '销量',
])

# 写入表头
csv_writer.writeheader()

# 打开浏览器
driver = ChromiumPage()

# 访问网站
driver.get('https://www.taobao.com/')

# 监听数据包
driver.listen.start('h5/mtop.relationrecommend')

# 输入商品关键字
driver.ele('css:#q').input('索尼a7m4')

# 进行点击搜索
driver.ele('css:.btn-search').click()

for page in range(5):
    print(f'正在采集第{page + 1}页的数据内容')
    # 设置延时
    time.sleep(2)
    # 让网页数据下滑到最下方
    driver.scroll.to_bottom()
    # 等待数据包加载
    resp = driver.listen.wait()
    # 获取响应数据
    text = resp.response.body
    info = re.findall('mtopjsonp\d+\((.*)', text)[0].replace(')', '')
    # 转数据类型
    json_data = json.loads(info)
    # 根据键值对取值, 提取商品信息所在列表
    items = json_data['data']['itemsArray']
    # for循环遍历, 提取列表里面元素
    for index in items:
        # 提取数据保存字典中
        area_info = index['procity'].split(' ')
        dit = {
            '标题': index['title'].replace('<span class=H>', '').replace('</span>', ''),
            '价格': index['priceWap'],
            '销量': index['realSales'].replace('人付款', '').replace('+', ''),
        }
        # 写入数据
        csv_writer.writerow(dit)
        print(dit)
    # 点击下一页按钮并等待页面加载
    next_button = driver.ele('css:.next-btn.next-medium.next-btn-normal.next-pagination-item.next-next')
    next_button.click()





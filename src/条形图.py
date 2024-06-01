import time
from my_package import my_csv
import re
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置全局中文字体为宋体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def get_average(lists):
    length = len(lists)
    average = sum(lists) / length
    return average


def extract_first_number(s):
    match = re.search(r'(\d+)(万|千)?', s)
    if match:
        number = int(match.group(1))
        unit = match.group(2)
        if unit == '万':
            number *= 10000
        elif unit == '千':
            number *= 1000
        return number
    else:
        return None


def is_in_tuple(tuple0, num0):
    if tuple0[0] <= num0 <= tuple0[1]:
        return True
    else:
        return False


def get_section(nums):
    # nums = [3, 4, 7, 8]
    section_tuples = []
    min_num = min(nums)
    max_num = max(nums)
    sum_length = max_num - min_num
    section_length = int(sum_length / 10)
    if section_length < 10:
        section_length = 10
    else:
        temp = int(section_length / 10)
        section_length = (temp + 1) * 10
    temp = int(min_num / 10) * 10
    left = temp + 1
    right = temp + section_length
    while right < max_num:
        section_tuple = (left, right)
        section_tuples.append(section_tuple)
        temp = right
        left = temp + 1
        right = temp + section_length
    return section_tuples


def get_dict(datas):
    lists = []

    my_dict = {}
    # datas = my_csv.read_to_csv(filename)
    del datas[0]

    for data in datas:
        string = data[2]
        temp = extract_first_number(string)
        if temp:
            lists.append(float(data[1]))
        else:
            continue

    sections = get_section(lists)

    for section in sections:
        my_dict[section] = []
    for data in datas:
        for section in sections:
            price = float(data[1])
            if not is_in_tuple(section, price):
                continue
            else:
                string = data[2]
                temp = extract_first_number(string)
                if temp:
                    my_dict[section].append(temp)
    return my_dict


def show_bar_plot(data, label, product_name):
    plt.bar(label, data, color='skyblue', width=0.5)
    # 添加标题和标签
    plt.title('{}不同价格区间的平均销售量'.format(product_name))
    plt.xlabel('价格区间')
    plt.ylabel('平均销售量')
    # 显示图形
    plt.show()


if __name__ == '__main__':
    name_dict = {
        "cleaning_钢笔": (1, 10000),
        "cleaning索尼": (1, 10000),
        "iPhone14": (1, 100),
        "奥林巴斯": (500, 1500),
        "充电宝": (1, 800),
        "防晒霜": (1, 400),
        "钢笔": (1, 1000),
        "护手霜": (10, 170),
        "闹钟": (1, 1000),
        "尼康d810": (1, 200),
        "索尼a7m4": (1000, 10000)
    }

    for name, limit in name_dict.items():
        clean_data = []
        filename = os.path.join(os.path.dirname(__file__), '..', 'data', f'{name}.csv')
        print(f"Attempting to read file: {filename}")  # 调试信息

        try:
            my_data = my_csv.read_to_csv(filename)
        except FileNotFoundError:
            print(f"File not found: {filename}")
            continue  # 跳过不存在的文件，继续处理下一个文件

        del my_data[0]
        for data in my_data:
            if is_in_tuple(limit, float(data[1])):
                clean_data.append(data)
            else:
                pass

        dic = get_dict(clean_data)

        labels = []
        datas = []
        for key, value in dic.items():
            if len(value) == 0:
                break

            datas.append(get_average(value))
            labels.append("{}-{}".format(key[0], key[1]))

        show_bar_plot(datas, labels, name)
        time.sleep(1)

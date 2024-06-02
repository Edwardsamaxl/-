import os
import time
from my_package import my_csv
import re
import matplotlib.pyplot as plt


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


def show_bing_plot(data, label, product_name):
    # 绘制饼图
    plt.figure(figsize=(8, 5))
    plt.pie(data, labels=label, autopct='%1.1f%%', startangle=140)
    plt.title('{}不同价格区间的平均销售量占比'.format(product_name))
    plt.axis('equal')  # 使饼图呈圆形
    plt.show()



if __name__ == '__main__':
    name_dict = {
        "索尼a7m4": (1, 20000),
        "钢笔": (1, 10000),
        "cleaning_钢笔": (1, 10000),
        "cleaning_索尼a7m4_": (1, 20000),
        # "cleaning_iPhone14_": (1, 10000),
        "cleaning_小米充电宝_10000": (1, 10000),
        "cleaning_三只松鼠每日坚果_750g": (1, 10000),
        # "cleaning_塑料袋_": (1, 10000),
        "cleaning_iPhone14_壳": (1, 10000)
    }
    for name, limit in name_dict.items():
        clean_data = []
        filename = os.path.join(os.path.dirname(__file__), '..', 'data', f'{name}.csv')

        my_data = my_csv.read_to_csv(filename)
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

        show_bing_plot(datas, labels, name)
        time.sleep(1)

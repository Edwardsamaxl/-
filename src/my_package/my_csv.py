import csv

def read_to_csv(file_path='2221.csv'):
    """
    读取 CSV 文件，并以列表形式返回其中的数据。

    参数：
    file_path (str): CSV 文件的路径。

    返回：
    list: 包含 CSV 文件数据的列表，每行数据作为一个子列表。
    """
    datas = []
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data = []
            for item in row:
                data.append(item)
            datas.append(data)
    return datas

def write_to_csv_row(data, filename):
    # 按需打开文件，如果文件不存在则创建新文件
    # data = ["你好", "那英", "SV文件中表达果要保存的内容有中文，而且之后需要用Excel打开文件，那么需要选用utf-8-sig编码。SV文件中表达段落层次感阿信啊。"]
    with open(filename, 'a', encoding="utf-8", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)

def write_to_csv_all(datas, filename):
    # 按需打开文件，如果文件不存在则创建新文件
    # data = ["你好", "那英", "SV文件中表达果要保存的内容有中文，而且之后需要用Excel打开文件，那么需要选用utf-8-sig编码。SV文件中表达段落层次感阿信啊。"]
    with open(filename, 'a', encoding="utf-8", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for data in datas:
            csv_writer.writerow(data)


if __name__ == '__main__':
    a = read_to_csv('a.csv')
    print(a)

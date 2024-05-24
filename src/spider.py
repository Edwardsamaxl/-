import csv
import parsel as parsel
import requests
import time
import os

# 获取当前文件所在目录的父目录路径
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)

# 构建data目录的路径
data_dir = os.path.join(parent_dir, 'data')

# 生成csv文件的路径
csv_file_path = os.path.join(data_dir, '奥林巴斯e-m10.csv')

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerow(['title', 'price', 'shop', 'detail_url'])
headers = {
    'Cookie':'__jdv=76161171|cn.bing.com|-|referral|-|1716282080094; __jdu=17162820800941433364055; 3AB9D23F7A4B3CSS=jdd03VXVUCOQYAYIGUFWIR72YCBVI4KG4Y5HDHHBRJJ6E42WS7GMQVOGFR4EBDMCH374VGGSAGGSC7LVITDVLZ2BQHXFWE4AAAAMPTJRDAAQAAAAADMCKMYO2NLBZPMX; _gia_d=1; areaId=1; ipLoc-djd=1-2800-0-0; shshshfpa=6f54acfc-a8bf-fd5a-41d6-4f82b0ee1733-1716282081; shshshfpx=6f54acfc-a8bf-fd5a-41d6-4f82b0ee1733-1716282081; mba_muid=17162820800941433364055; mba_sid=17162821461658499573938918521.1; wlfstk_smdl=o2zgjslqnyxif5bxtcclweh2v0eucub0; TrackID=1KtTnuqUEsgNpA926tCDZE6pODxZ90QDAnX5LcDBC_-rFMs9vL7olpwaBlVFU3cJMj1GxDMcIxcs-XurSgNLYYg3J0hq5rbSLyTbvGJcPTLvpqSHyUpKrFwhEe1HlBFNY; thor=573FD77DF81A631706ED214ABDD4F7B64F961B6E124D7949BC685D27ED2556FD818666554451781398752B6F0A1A0EBEC6CF5039D91BF2AFF4F40643695F979A4F4CD0393985D75B83E9B07A825365B2CCF8A0B20C5C2B43656BC0F4E3B75C498BE41499E7D525BB2223AD5ACA6425A1F1FD5633F507ABA25C78C17CF2F0F8BB197035586148E94ACD514E3E996C803C57901FAD80B5FA0C2B7A86177241637A; flash=2_Cu0Hyg3CAge69xyY2AWZ6hQzZ5OxZlxHn5L_iTFlyx-c5Hy82p5RqEDeUmWOsC5h8tsZuVm-0dKEiBe_q_dlLuKV8kVjlDkMPKVzHWShnCOxHOHQhMuVxHJu0Ffg6wCP-PaxJlWWSEe9y_bmv1DkVPz7OjXOaR_N5-Jp2qGhnHk*; pinId=OW3K76lL4rY0ZumHtz5yW7V9-x-f3wj7; pin=jd_72063071790b3; unick=jd_186667lov; ceshi3.com=000; _tp=VM3kwDQ96YGZC2l9Te%2BevORnvmlvL2EwoXpMOG0W6jk%3D; _pst=jd_72063071790b3; jsavif=1; jsavif=1; xapieid=jdd03VXVUCOQYAYIGUFWIR72YCBVI4KG4Y5HDHHBRJJ6E42WS7GMQVOGFR4EBDMCH374VGGSAGGSC7LVITDVLZ2BQHXFWE4AAAAMPTJRDAAQAAAAADMCKMYO2NLBZPMX; qrsc=1; __jda=143920055.17162820800941433364055.1716282080.1716282080.1716282080.1; __jdb=143920055.9.17162820800941433364055|1.1716282080; __jdc=143920055; rkv=1.0; shshshfpb=BApXcXsJrmepAogLsWvgT7vMfJvULKKbpBlRpJ65o9xJ1MqFYUYC2; 3AB9D23F7A4B3C9B=VXVUCOQYAYIGUFWIR72YCBVI4KG4Y5HDHHBRJJ6E42WS7GMQVOGFR4EBDMCH374VGGSAGGSC7LVITDVLZ2BQHXFWE4',
    'Origin': 'https://search.jd.com',
    'Referer': 'https://search.jd.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}
s = 1
for page in range(1, 20): #1-20页
    t = int(time.time() * 1000)
    if page % 2 == 1:
        body = '{"keyword":"奥林巴斯e-m10","suggest":"3.def.0.~SAK8|MIXTAG_SAK8R,BUNCH_A_SAK8_R,SAK8_M_AM_L34160,SAK8_M_GUD_R,SAK8_S_AM_R,SAK8_D_HSP_R,SAK8_O_QJCON_L47824,SAK8_SC_PD_R,SAK8_SM_PB_R,SAK8_SM_PRK_R,SAK8_SM_PRC_R,SAK8_SM_PRR_R,SAK8_SS_PM_R|"' \
               ',"wq":"奥林巴斯e-m10","pvid":"d8f4d2565ffd46f082daf231963f0e0d","isList":0,"page":"' + str(
        page) + '","s":"' + str(s) + '",,"click":"0","show_items":""}'
    else:
        body = '{"keyword":"奥林巴斯e-m10","suggest":"3.def.0.~SAK8|MIXTAG_SAK8R,BUNCH_A_SAK8_R,SAK8_M_AM_L34160,SAK8_M_GUD_R,SAK8_S_AM_R,SAK8_D_HSP_R,SAK8_O_QJCON_L47824,SAK8_SC_PD_R,SAK8_SM_PB_R,SAK8_SM_PRK_R,SAK8_SM_PRC_R,SAK8_SM_PRR_R,SAK8_SS_PM_R|","wq":"奥林巴斯e-m10","pvid":"d8f4d2565ffd46f082daf231963f0e0d","page":"' + str(
        page) + '","s":"' + str(s) + '","scrolling":"y","tpl":"1_M","isList":0,"show_items":""}'
    if page==1:
        s=27
    if page==2:
        s=59
    if page==3:
        s=91
    if page>3:
        s+=30
    params = {
        'appid': 'search-pc-java',
        'functionId': 'pc_search_adv_Search', # 改
        'client': 'pc',
        'clientVersion': '1.0.0',
        't': str(t),
        'body': body,
        'loginType': '3',
        'uuid': '143920055.17162820800941433364055.1716282080.1716282080.1716296067.2', # 改
        # 'area': '18_1482_48942_49058',
        # 'h5st': '20231017205657848;g5giig9tnm63gij2;f06cc;tk03wbde31c7218nmTOuI4vmUG1gibUwyDKLNpF6B_t1uk9ukpSq3k_k19h74PyUWE_Fz9mV-ggz4JCtsVbQZVSId9dC;825dbf6bd60713fa1ddad5e95d169108;4.1;1697547417848;ee3cf7f6b94dc20e9265d83066bb9ceece4bb89e2b7e8bf5afb1bfd928788174bfa06c210ddd4437d8a2e234330c3a3980b96c3953b1ab788029ae792b39e113ccac142f09e3a1fa8c3f25055353b835ed0bf65228424626b8a9e1d2c030999d9be97a9dee9fb20116ceb0deb8736546109bc1cf5b91d1dfa2b39c79b3b0f0a5a036cdc921a1f147179b291c830dc87a6d3d0c3885fe721d5f0391a55bb4bf663963282084e04c7f24e6d3bcb219f4cb08a33c86f2c515c368479ab2fffd0f4935b373832965c1ba9aa292710f7023e99dac2e1bde15cd796fe1601c5425e954a8cebb66dc24031fb337c7d79d2a6f46c875d77cbc102770fd5125f99aaa366d5abac9c006c2f0275731844dd1353f808489e029e35b485616771b972ae3bb95',
        'x-api-eid-token': 'jdd03VXVUCOQYAYIGUFWIR72YCBVI4KG4Y5HDHHBRJJ6E42WS7GMQVOGFR4EBDMCH374VGGSAGGSC7LVITDVLZ2BQHXFWE4AAAAMPTNKRLYQAAAAACHKFPDJMA2Y7ZMX',
    }
    # 改
    url = "https://search.jd.com/Search?keyword=%E5%A5%A5%E6%9E%97%E5%B7%B4%E6%96%AFe-m10&enc=utf-8&suggest=3.def.0.~SAK8|MIXTAG_SAK8R,BUNCH_A_SAK8_R,SAK8_M_AM_L34160,SAK8_M_GUD_R,SAK8_S_AM_R,SAK8_D_HSP_R,SAK8_O_QJCON_L47824,SAK8_SC_PD_R,SAK8_SM_PB_R,SAK8_SM_PRK_R,SAK8_SM_PRC_R,SAK8_SM_PRR_R,SAK8_SS_PM_R|&wq=%E5%A5%A5%E6%9E%97%E5%B7%B4%E6%96%AF&pvid=d8f4d2565ffd46f082daf231963f0e0d"
    # 1. 发送请求 (访问网站)
    response = requests.get(url=url, params=params, headers=headers)
    # 2. 提取数据 将需要的内容提取出来
    html_data = response.text
    # 提取网页源代码当中的内容
    select = parsel.Selector(html_data)
    # 拿到了每个商品所属的标签
    lis = select.xpath('//ul[@class="gl-warp clearfix"]/li')
    for li in lis:
        title = li.xpath('string(.//div[@class="p-name p-name-type-2"])').get("").strip()
        price = li.xpath('string(.//div[@class="p-price"])').get("").strip()
        shop = li.xpath('string(.//div[@class="p-shop"])').get("").strip()
        # commit = li.xpath('string(.//div[@class="p-commit"])').get("").strip()
        detail_url = "https:" + li.xpath('.//div[@class="p-name p-name-type-2"]/a/@href').get("")
        print(title, price, shop, detail_url)
        # print(price,commit)
        # 3. 保存数据
        with open(csv_file_path, mode='a', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow([title, price, shop, detail_url])
            # csv.writer(f).writerow([price,commit])
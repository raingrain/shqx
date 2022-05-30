import matplotlib.pyplot as plt
import pandas as pd


def aboutAQI():
    while True:
        print("=" * 50)
        year = input('查询上海市2014年至2020年之间某年每月空气质量指数，请输入2014至2020之间的整数，输入0退出：')
        if year.isdigit() and 2014 <= int(year) <= 2020:
            draw(int(year))
            continue
        elif year == '0':
            return
        else:
            print('输入错误，请重新输入')


def draw(year):
    df = pd.read_excel('data/AQI.xlsx')

    li = []
    for i in range(len(df.loc[:, '统计日期'])):
        if int(df.loc[:, '统计日期'][i][:4]) == year:
            li.append(i)
    df_year = df.iloc[li]
    for i in range(len(df_year.loc[:, '统计日期'])):
        df_year.loc[:, '统计日期'].values[i] = df_year.loc[:, '统计日期'].values[i][0:7]
    grouped = df_year.groupby(['统计日期'])
    keys, datas = [], []
    for key, data in grouped:
        keys.append(key)
        datas.append(data.loc[:, 'AQI指数'])

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(14, 8))
    plt.boxplot(datas,  # 每个月AQI组成的12个ndarray
                labels=keys,  # 12个月份组成的ndarray
                showmeans=True,  # 显示均值
                meanline=True,
                flierprops={'marker': 'D', 'markersize': 5, 'markerfacecolor': 'red', 'markeredgewidth': '0'},  # 异常值属性
                patch_artist=True,
                whiskerprops={'linestyle': '--'},
                capprops={'linestyle': '-'},
                boxprops={'color': 'black', 'facecolor': '#e9e9e9'})  # 箱体格式
    plt.title('上海市{}年每月空气质量指数(AQI)箱线统计图'.format(year))
    plt.xlabel('{}年'.format(year))
    plt.ylabel('空气质量指数(AQI)', color='#666666')
    plt.yticks(color='#666666')
    plt.grid()

    plt.tight_layout()
    plt.savefig('images/{}年/上海市{}年每月空气质量指数(AQI)箱线统计图.png'.format(year, year))
    print('已保存至images/{}年/上海市{}年每月空气质量指数(AQI)箱线统计图.png'.format(year, year))
    plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def aboutSun():
    while True:
        print("=" * 50)
        year = input('查询上海市2000年至2020年之间某年每月日照总时数，请输入2000至2020之间的整数，输入0退出：')
        if year.isdigit() and int(year) in [x for x in range(2000, 2021)]:
            draw(year)
            continue
        elif year == '0':
            return
        else:
            print('错误，请重新输入')


def draw(year):
    df = pd.read_excel('data/日照时数.xlsx')

    begin = year + '-01'
    end = year + '-12'
    x1 = 0
    x2 = 0
    length = len(df.loc[:, '月度标识'])
    for i in range(length):
        if df.loc[:, '月度标识'][i] == begin:
            x1 = i
        elif df.loc[:, '月度标识'][i] == end:
            x2 = i

    df_plt = df.iloc[x1:x2 + 1, :]
    df_plt.set_index('月度标识', inplace=True)
    df_plt_max = df_plt.loc[:, '日照时数(h)'].max()

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    df_plt.plot.barh(rot=-45, figsize=(14, 8), color='#FF6600')
    plt.title('上海市{}年每月日照时数(h)柱状统计图'.format(year))
    plt.xlabel('日照时数(h)')
    plt.ylabel('月份')
    plt.xticks(np.arange(0, int(df_plt_max + 20), step=20), color='#FF6600')
    plt.grid(axis='x')

    plt.tight_layout()
    plt.savefig('images/{}年/上海市{}年每月日照时数柱状统计图.png'.format(year, year))
    print('已保存至images/{}年/上海市{}年每月日照时数柱状统计图.png'.format(year, year))
    plt.show()

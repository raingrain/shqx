import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def aboutRain():
    while True:
        print("=" * 50)
        year = input('查询上海市2000年至2020年之间某年每月降水量，请输入2000至2020之间的整数，输入0退出：')
        if year.isdigit() and int(year) in [x for x in range(2000, 2021)]:
            draw(year)
            continue
        elif year == '0':
            return
        else:
            print('错误，请重新输入')


def draw(year):
    df = pd.read_excel('data/降水量.xlsx')

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
    df_plt_max = df_plt.loc[:, '降水量(mm)'].max()

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    df_plt.plot.bar(rot=45, figsize=(14, 8), color='#0099FF')
    plt.plot(df_plt.index, df_plt.loc[:, '降水量(mm)'], color="black", linestyle=":", marker="v", markersize=10,
             markerfacecolor="red", markeredgewidth="0")
    plt.yticks(np.arange(0, int(df_plt_max + 20), step=20), color='#3399FF')
    plt.title('上海市{}年每月降水量(mm)折线与柱状统计图'.format(year))
    plt.xlabel('月份')
    plt.ylabel('降水量(mm)', color='#3399FF')
    plt.legend(['变化折线', '柱形概览'])
    plt.grid(axis='y')

    plt.tight_layout()
    plt.savefig('images/{}年/上海市{}年每月降水量折线与柱状统计图.png'.format(year, year))
    print('已保存至images/{}年/上海市{}年每月降水量折线与柱状统计图.png'.format(year, year))
    plt.show()

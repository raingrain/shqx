import matplotlib.pyplot as plt
import pandas as pd


def aboutHT():
    while True:
        print("=" * 50)
        year = input('查询上海市2000年至2020年之间某年每月平均相对湿度和平均温度，请输入2000至2020之间的整数，输入0退出：')
        if year.isdigit() and int(year) in [x for x in range(2000, 2021)]:
            draw(year)
            continue
        elif year == '0':
            return
        else:
            print('错误，请重新输入')


def draw(year):
    df_1 = pd.read_excel('data/平均相对湿度.xlsx')

    begin = year + '-01'
    end = year + '-12'
    x1 = 0
    x2 = 0
    length = len(df_1.loc[:, '月度标识'])
    for i in range(length):
        if df_1.loc[:, '月度标识'][i] == begin:
            x1 = i
        elif df_1.loc[:, '月度标识'][i] == end:
            x2 = i
    df_plt_1 = df_1.iloc[x1:x2 + 1, :]
    x = df_plt_1.loc[:, '月度标识']

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fig, ax1 = plt.subplots()
    fig.set_size_inches(14, 8)
    color = 'tab:green'
    ax1.plot(x, df_plt_1.loc[:, '平均相对湿度(%)'], color="green", linestyle="--", marker="*", markersize=10,
             markerfacecolor="blue", markeredgewidth="0")
    ax1.set_xlabel('月份')
    ax1.set_ylabel('平均相对湿度(%)', color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    df_2 = pd.read_excel('data/平均温度.xlsx')
    df_plt_2 = df_2.iloc[x1:x2 + 1, :]

    color = 'tab:orange'
    # 翻转
    ax2 = ax1.twinx()
    ax2.plot(x, df_plt_2.loc[:, '平均温度(℃)'], color="orange", linestyle="-.", marker="P", markersize=10,
             markerfacecolor="red", markeredgewidth="0")
    ax2.set_ylabel('平均温度(℃)', color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax1.grid()
    ax1.set_title('上海市{}年每月平均相对湿度(%)和平均温度(℃)对比折线图'.format(year))
    fig.legend(['平均相对湿度(%)', '平均温度(℃)'], loc='upper right')

    fig.tight_layout()
    plt.savefig('images/{}年/上海市{}年每月平均相对湿度和平均温度对比折线图.png'.format(year, year))
    print('已保存至images/{}年/上海市{}年每月平均相对湿度和平均温度对比折线图.png'.format(year, year))
    plt.show()

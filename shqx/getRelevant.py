import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def aboutRelevant():
    while True:
        print('=' * 50)
        tmp = input('请输入a/b选择上海市2000年至2020年间两种气象数据绘制散点图（包含一阶拟合）/所有气象数据绘制散点矩阵图，输入0退出：')
        if tmp == 'a':
            i = input("请输入1/2/3/4来选择平均温度/平均相对湿度/日照时数/降水量之间的一个作为拟合直线的x：")
            j = input("请输入1/2/3/4来选择平均温度/平均相对湿度/日照时数/降水量之间的一个作为拟合直线的y：")
            if i.isdigit() and j.isdigit():
                if 1 <= int(i) <= 4 and 1 <= int(j) <= 4:
                    draw_a(int(i), int(j))
                else:
                    print('输入错误，请重新输入')
            else:
                print('输入错误，请重新输入')
        elif tmp == 'b':
            draw_b()
        elif tmp == '0':
            break
        else:
            print('输入错误，请重新输入')


# 两个数据之间的
def draw_a(i, j):
    df1 = pd.read_excel('data/平均温度.xlsx')
    df2 = pd.read_excel('data/平均相对湿度.xlsx')
    df3 = pd.read_excel('data/日照时数.xlsx')
    df4 = pd.read_excel('data/降水量.xlsx')
    df_plt = pd.merge(left=pd.merge(left=pd.merge(left=df1, right=df2), right=df3), right=df4)

    x = df_plt.iloc[:, i:i + 1].values
    x_list = []
    for x_num in x:
        x_list.append(*x_num)

    y = df_plt.iloc[:, j:j + 1].values
    y_list = []
    for y_num in y:
        y_list.append(*y_num)

    cof = np.polyfit(x_list, y_list, 1)
    des = "拟合线y=%.1fx%+.1f" % tuple(cof)
    p1 = np.poly1d(cof)
    y1 = p1(df_plt.iloc[:, i:i + 1])

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(14, 8))
    plt.scatter(x_list, y_list, marker='H', color='#687fa5')
    plt.plot(df_plt.iloc[:, i], y1, color='r')
    plt.axvline(np.array(x_list).mean(), color="#687fa5", linewidth=1, linestyle='--')
    plt.axhline(np.array(y_list).mean(), color="#687fa5", linewidth=1, linestyle='--')
    plt.xlabel(df_plt.columns[i])
    plt.ylabel(df_plt.columns[j])
    plt.legend([des])
    plt.title('上海市20年间{}与{}散点图'.format(df_plt.columns[i], df_plt.columns[j]))

    plt.tight_layout()
    plt.savefig('images/上海市20年间{}与{}散点图.png'.format(df_plt.columns[i], df_plt.columns[j]))
    print('已保存至images/上海市20年间{}与{}散点图.png'.format(df_plt.columns[i], df_plt.columns[j]))
    plt.show()


# 所有数据之间的
def draw_b():
    df1 = pd.read_excel('data/平均温度.xlsx')
    df2 = pd.read_excel('data/平均相对湿度.xlsx')
    df3 = pd.read_excel('data/日照时数.xlsx')
    df4 = pd.read_excel('data/降水量.xlsx')
    df_plt = pd.merge(left=pd.merge(left=pd.merge(left=df1, right=df2), right=df3), right=df4)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    pd.plotting.scatter_matrix(df_plt.iloc[:, 1:5], diagonal='kde', marker='^', color='red', figsize=(14, 8))

    plt.tight_layout()
    plt.savefig('images/上海市20年间每月平均温度、平均相对湿度、日照时数与降水量散点矩阵图.png')
    print('已保存至images/上海市20年间每月平均温度、平均相对湿度、日照时数与降水量散点矩阵图')
    plt.show()

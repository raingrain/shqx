import getAQI
import getHT
import getRain
import getSun
import getRelevant


def main():
    # 主逻辑输入，输入不同的数字可以进入不同的功能，进入各自功能后可以输入0退出到主逻辑
    print('本程序提供近十到二十年之间每年每月上海市相关气象数据查询与分析')
    while True:
        print("=" * 50)
        temp = input('输入您要查询的数据：0、退出，1、AQI，2、平均相对湿度和平均温度，3、降水量，4、日照时数，5、相关性分析：')
        if temp == '0':
            print('再见，感谢您的使用！\n本程序作者：冯祥旭，李俊彬\n更多数据请访问https://www.gtarsc.com/')
            return
        elif temp == '1':
            getAQI.aboutAQI()
        elif temp == '2':
            getHT.aboutHT()
        elif temp == '3':
            getRain.aboutRain()
        elif temp == '4':
            getSun.aboutSun()
        elif temp == '5':
            getRelevant.aboutRelevant()
        else:
            print('输入错误，请重新输入')



if __name__ == '__main__':
    main()

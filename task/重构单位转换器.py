# !/usr/bin/env Python
# -*- coding:utf-8 -*-
# chatbot.py
# A chat robot demo
# author: XueZhiQiang


class Transfer():
    def __init__(self,name):
        """初始化属性（转换器的名称）"""
        self.name = name

    def program_ui(self):
        """程序ui（判断部分）"""
        while True:
            try:  # 异常处理,防止输入（AC,AF,AM,AI..）
                choose = self.welcome(self.name)  # 欢迎菜单
                if choose == 'Q' or choose == 'q':  # 判断退出
                    break
                elif choose == 'T' or choose == 't':  # 判断是否需要温度转换
                    temp = input("温度转换,示例:(1华氏度:1F)(1摄氏度:1C)：")
                    temp.endswith('C') and Temperature().select_ce(temp)
                    temp.endswith('F') and Temperature().select_fa(temp)
                    temp.endswith('C') or temp.endswith('F') or self.error('C','F')
                elif choose == 'L' or choose == 'l':  # 判断是否需要长度转换
                    length = input("请输入长度,示例:(1米:1M)(1英寸:1I)：")
                    length.endswith('M') and Length().select_me(length)
                    length.endswith('I') and Length().select_in(length)
                    length.endswith('M') or length.endswith('I') or self.error('M','I')
                elif choose == 'C' or choose == 'c':  # 判断是否需要货币转换
                    currency = input("请输入货币数,示例:(1人民币:1C)(1美元:1U)：")
                    currency.endswith('C') and Currency().select_cn(currency)
                    currency.endswith('U') and Currency().select_us(currency)
                    currency.endswith('C') or currency.endswith('U') or self.error('C','U')
            except Exception as e:
                print('输入错误,格式为("整数"字母)',e)
                input()

    def welcome(self,name):
        """欢迎主菜单"""
        print (f'欢迎使用{name}转换器'.center(50,'*'))
        menu = {                    
            'T':'温度转换',
            'L':'长度转换',
            'C':'货币转换'}
        for k,v in menu.items():
            print(f'输入{k}:进入{v}')
        print ('退出请输入Q'.center(55,'*'))
        return input('请从（T L C）选择输入一个:')

    def error(self,x,y):
        """输错后缀提示"""
        print(f'输入错误,格式为(整数+大写字母{x}或{y})')
        input()


class Temperature():
    """温度转换两个功能"""
    def select_fa(self,units):
        self.units = units
        self.units = self.units.strip('F')
        result = (float(self.units) - 32)/(9 / 5)  # 反向公式
        print(f'{self.units}华氏度转换后为：{result}摄氏度')
        input()        

    def select_ce(self,units):
        self.units = units
        self.units = self.units.strip('C')
        result = (9 / 5) * float(self.units) + 32  # 转换公式
        print(f'{self.units}摄氏度转换后为：{result}华氏度')
        input()


class Length():
    """长度转换两个功能"""
    def select_me(self,units):
        self.units = units
        self.units = self.units.strip('M')
        result = float(self.units) / 0.0254
        print(f'{self.units}米转换后为：{result}英寸')
        input()

    def select_in(self,units):
        self.units = units
        self.units = self.units.strip('I')
        result = float(self.units) * 0.0254
        print(f'{self.units}英寸转换后为：{result}米')
        input()


class Currency():
    """货币转换两个功能"""
    def select_cn(self,units):
        self.units = units
        self.units = self.units.strip('C')
        result = float(self.units) / 7.13
        print(f'{self.units}人民币转换后为：{result}美元')
        input()

    def select_us(self,units):
        self.units = units
        self.units = self.units.strip('U')
        result = float(self.units) * 7.13
        print(f'{self.units}美元转换后为：{result}人民币')
        input()


def main():
    run = Transfer('万能')
    run.program_ui()

if  __name__ == "__main__":
    main()
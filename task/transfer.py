# v1
def transfer1():
    menu = {
            "T":"温度转换",
            "L":"长度转换",
            "C":"货币转换"T
    }
    for k, v in menu.items():
        print(k, v)
    enter = input("请根据屏幕提示输入转换单位的英文缩写")

    if enter == "T":
        tempera = input("请输入温度，例如1f或1c")
        if tempera.endswith("c"):
            tempera = float(tempera.strip("c"))
            tempera = 9/5*tempera+32
            print(f"转换后为{round(tempera,2)}f")
        elif tempera.endswith("f"):
            tempera = float(tempera.strip("f"))
            tempera = 5/9*(tempera-32)
            print(f"转换后为{round(tempera,2)}c")
    elif enter == "L":
        length = input("请输入长度,例如1m或1ft")
        if length.endswith("m"):
            length = float(length.strip("m"))
            length = length*3.2808
            print(f"转换后为{round(length,2)}ft")
        elif length.endswith("f"):
            length = float(length.strip("f"))
            length = length/3.2808
            print(f"转换后为{round(length,2)}m")
    elif enter == "C":
        currency = input("请输入金额,例如1$或1￥")
        if currency.endswith("$"):
            currency = float(currency.strip("$"))
            currency = currency*7.1382
            print(f"转换后为{round(currency,2)}￥")
        elif currency.endswith("￥"):
            currency = float(currency.strip("￥"))
            currency = currency/7.1382
            print(f"转换后为{round(currency,2)}$") 

# v2
# 
def transfer_by_type(data, from_v, to_v):
    # data = input("请输入金额,例如1$或1￥")
    if data.endswith(from_v):
        data = float(data.strip(from_v))
        data = calc_by_type(data, f"{from_v}-{to_v}")
        print(f"转换后为{round(data,2)}{to_v}")
    elif data.endswith(to_v):
        data = float(data.strip(to_v))
        data = calc_by_type(data, f"{to_v}-{from_v}")
        print(f"转换后为{round(data,2)}{from_v}")  


def calc_by_type(data, trans_type="$-￥"):
    if trans_type == '$-￥':
        return data*7.1382
    elif trans_type == '￥-$':
        return data/7.1382

def transfer2():
    menu = {
            "T":"温度转换",
            "L":"长度转换",
            "C":"货币转换"
    }
    for k, v in menu.items():
        print(k, v)
    enter = input("请根据屏幕提示输入转换单位的英文缩写")

    if enter == "T":
        tempera = input("请输入温度，例如1f或1c")
        if tempera.endswith("c"):
            tempera = float(tempera.strip("c"))
            tempera = 9/5*tempera+32
            print(f"转换后为{round(tempera,2)}f")
        elif tempera.endswith("f"):
            tempera = float(tempera.strip("f"))
            tempera = 5/9*(tempera-32)
            print(f"转换后为{round(tempera,2)}c")
    elif enter == "L":
        length = input("请输入长度,例如1m或1ft")
        if length.endswith("m"):
            length = float(length.strip("m"))
            length = length*3.2808
            print(f"转换后为{round(length,2)}ft")
        elif length.endswith("f"):
            length = float(length.strip("f"))
            length = length/3.2808
            print(f"转换后为{round(length,2)}m")
    elif enter == "C":
        currency = input("请输入金额,例如1$或1￥")
        transfer_by_type(currency, "$", "￥")

# v3
class Transfer:
    def __init__(self, data):
        self.data = data
        self.trans_type = self.build_transfer_type()  # 根据输入data后缀，构造类型

    def transfer_by_type(self):
        from_v, to_v = self.trans_type.split('-')
        if self.data.endswith(from_v):
            data = float(self.data.strip(from_v))
            data = self.calc_by_type(data)
            print(f"转换后为{round(data,2)}{to_v}")
        elif self.data.endswith(to_v):
            data = float(self.data.strip(to_v))
            data = self.calc_by_type(data)
            print(f"转换后为{round(data,2)}{from_v}")  

    def calc_by_type(self, data):
        if self.trans_type == '$-￥':
            return data*7.1382
        elif self.trans_type == '￥-$':
            return data/7.1382

    def build_transfer_type(self):
        if self.data.endswith('$'):
            return "$-￥"
        elif self.data.endswith('￥'):
            return '￥-$'


def transfer3():
    menu = {
            "T":["温度转换","请输入温度，例如1f或1c"],
            # "L":"长度转换",
            "C":["货币转换","请输入金额,例如1$或1￥"]
    }
    for k, v in menu.items():
        print(k, v[0])
    enter = input("请根据屏幕提示输入转换单位的英文缩写")
    data = input(menu[enter][1])
    # if enter == "T":
    #     tempera = input("请输入温度，例如1f或1c")
    #     if tempera.endswith("c"):
    #         tempera = float(tempera.strip("c"))
    #         tempera = 9/5*tempera+32
    #         print(f"转换后为{round(tempera,2)}f")
    #     elif tempera.endswith("f"):
    #         tempera = float(tempera.strip("f"))
    #         tempera = 5/9*(tempera-32)
    #         print(f"转换后为{round(tempera,2)}c")
    # elif enter == "L":
    #     length = input("请输入长度,例如1m或1ft")
    #     if length.endswith("m"):
    #         length = float(length.strip("m"))
    #         length = length*3.2808
    #         print(f"转换后为{round(length,2)}ft")
    #     elif length.endswith("f"):
    #         length = float(length.strip("f"))
    #         length = length/3.2808
    #         print(f"转换后为{round(length,2)}m")
    # elif enter == "C":
    #     data = input("请输入金额,例如1$或1￥")
 
    t = Transfer(data)
    t.transfer_by_type()

if __name__ == "__main__":
    # transfer1()
    # transfer2()
    transfer3()
    
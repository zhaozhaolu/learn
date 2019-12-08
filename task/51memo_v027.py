#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 51memo_v027.py
# A memo demo 51备忘录, 使用函数+正则进行优化
# author: De8uG

"""
场景1：根据已有数据：统计本月共多少人面试，整理手机号列表
data = '''
○ 4.1日，共有4人面试，手机号分别是13812345678，15112345678，13812345678，15112345678
○ 4.5日，共有6人面试13812345678，15112345678，13812345678，15112345678，13812345678，15112345678
○ 4.7日，共有3人面试13812345678，1511234ss5678，13812345678
○ 4.8日，共有5人面试15112345678，13812345678，15112345678，13812345678，15112345678
4.30日，共有6人面试13812345678，15112345678，13812345678，15112345678，13812345678，15112345678
'''
# 思考：
# 1 如果只统计某个网段的手机号呢，比如138..
# 2 或者只统计真实存在的网段手机号呢，比如138，151，180类似这种真实有人用的网段[123xx|146xx]

- 场景2：有如下的多条备忘记录，请完成后续功能开发
memo_text = '''
1.1 去找小8写个程序
1.2 记一下王总的电话 139-1234-5678
1.3 修改Python程序的bug
1.4 路上买二斤西红柿，遇见卖鸡蛋的就买一斤
1.5 事情太多，忘了今天要干啥
'''
修改里面的日期格式为几月几日，比如1.1  改为 1月1日

- 场景3：
添加登陆验证功能，只限于个人使用
"""


import sys


__author__ = 'De8uG'


def welcome():
    "欢迎词儿！"
    desc = '51备忘录'.center(30, '-')
    print(desc)

    welcome = 'welcome'
    print(f'{welcome}', __author__)

    print('请输入备忘信息：')

# welcome()  # 不在函数定义之后直接用！

all_memo = []  
# 添加dict保存一条信息
"""
{
    'date': 1.1,
    'thing': 'python',
    'time': 30
}
{
    'time': 8,
    'thing': 'python',
}
"""


def input_memo():
    "输入备忘记录"
    try:
        is_add = True
        all_time = 0    
        while(is_add):  # 这是个循环输入
            in_date = input('日期：')
            in_thing = input('事件：')
            in_time = input('用时：')
            print('待办列表'.center(30, '-'))
            # one = '{date}, 处理{thing}, 用时{time}'.format(date=in_date, thing=in_thing, time=in_time)
            add_memo(in_date, in_thing, in_time)
            all_time += int(in_time)
            print_memo(all_time)
            is_add = input().strip() == 'y'
    except Exception as e:
        print('添加memo出错啦！', e)


def print_memo(all_time):
    "打印memo"
    num = 0
    for m in all_memo:
        num += 1
        print('%s:%s' % (num, m))

    print(f'共{len(all_memo)}条待办事项, 总时长：{all_time}。', end='')
    print('（y：继续添加，n: 退出）')


def add_memo(in_date, in_thing, in_time):
    "添加备忘记录"
    one = {}
    one['date'] = in_date
    one['thing'] = in_thing
    one['time'] = in_time
    all_memo.append(one)


def help():
    print("""usage: 
    -a or --add, 添加记录
    -d or --delete, 删除记录
    """)


def delete_memo():
    print('请自己完成函数，添加各种参数，对列表进行操作')


def modify_memo():
    pass


def main():
    """
    main: 程序主入口，当前文件单独运行时候从这里运行
    函数优化：每个函数尽量只干一件事儿！
    用sys模块添加系统参数
    """
    # print(sys.argv)
    try:
        if len(sys.argv) == 1:
            help()
        
        welcome()
        if sys.argv[1] in {"-h", "--help"}:
            help()
        elif sys.argv[1] in {"-a", "--add"}:
            input_memo()
        elif sys.argv[1] in {"-d", "--delete"}:
            delete_memo()
        else:
            help()
    except Exception as e:
        print(e)
        help()

if __name__ == '__main__':
    main()
'''
#1实现购物车程序
import sys

# keep the code below
goods = [
    {"name": "Computer", "price": 1999},
    {"name": "Mouse", "price": 10},
    {"name": "Yachts", "price": 20},
    {"name": "Airplane", "price": 998}
]


asset = int(sys.argv[1])
input_list = eval(sys.argv[2])

# write your code here
for i in input_list:
    if i>4:
        print("Please re-enter")
    elif i==0:
        break
    else:
        name_i=goods[i-1]["name"]
        price_i=goods[i-1]["price"]
        print(f"You want to buy: {name_i}")
        print(f"It is priced at: {price_i}")
        if price_i<=asset:
            asset-=price_i
            print("Purchase successful!")
        else:
            print("The balance is low, so go ahead and top up!")
            break
#2自定义异常
class MyError(Exception):
    def __init__(self, code):
        # write your code here:
        self.code=code
    def __str__(self):
        # write your code here:
        return str(self.code)
#3迭代器和斐波那契数列
class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        # write your code here:
        t=self.a
        self.a=self.a+self.b
        self.b=t
        return self.a
#4迭代器和偶数数列
class EvenIterator:
    def __init__(self, max_value):
        # write your code here:
        self.max_value=max_value
        self.i=-2
    def __iter__(self):
        return self

    def __next__(self):
        # write your code here:
        self.i+=2
        t=self.i
        if self.i>self.max_value:
            raise StopIteration()
        return t
#5使用偏函数求 n % 999 的结果
import functools
def division(m, n):
    return n % m
# write your code here:
result=functools.partial(division,999)
#6将字典的键和值组成新列表
def composition(dict_1: dict) -> list:
    result = []
    for i in dict_1:
        result.append(i)
        result.append(dict_1[i])
    return result
    # -- write your code here --
#7根据行边界符拆分字符串并找出最长行
def splitlines(src: str) -> str:
    """
    :param src: The source string needs to be processed
    :return: The maximum length of the string
    """
    # -- write your code here --
    list=src.splitlines()
    max=list[0]
    # for i in range(1,len(list)):

    #     if len(list[i])>len(max):
    #         max=list[i]
    # return max
    list.sort(key=len,reverse=True)
    return list[0]
'''
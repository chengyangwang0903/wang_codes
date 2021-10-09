# a=242
# b=hex(a)
# print("二进制：{1}，八进制：{2}，十六进制：{0}".format(b,bin(a),oct(a)))
# print(int(b,16))
# a="gsdag1"
# print(a[:])

#
# x=input("请输入英文名：")
# print(x.lower())
# print(x.upper())
# x1=x.lower()
# for i in range(len(x1)):
#     if i==0:
#         print(x1[i].upper(),end="")
#     else:
#         print(x1[i],end="")

# x=["caf","asag","bsag"]
#
# print(sorted(x,reverse=True))
# print(chr(ord("a")))

# def findid(n):
#     print(n)
#     return n
# id=input("输入用户id")
# print(findid(id))

#python前置练习题
'''#1
num=1
for i in range(9,0,-1):
    num=(num+1)*2
print("第一天摘了{}个桃子".format(num))
#2
molecular=2
denoinator=1
num=molecular/denoinator
sum=0
for i in range(20):
    sum+=num
    temp=denoinator
    denoinator=molecular
    molecular+=temp
    num=molecular/denoinator
print("该分数序列的前20项之和为：{}".format(sum))
#3
def sum(n):
    if n==1:
        return 1
    return n*sum(n-1)
num=0
for i in range(1,21):
    num+=sum(i)
print("前20项阶乘求和为：{}".format(num))
#4
menu=["土豆","马铃薯","洋芋","洋芋"]
menu=set(menu)
menu=list(menu)
print("菜单：",menu)
#5
str="abc"
def reversal(str):
    str1=""
    for i in range(len(str)-1,-1,-1):
        str1+=str[i]
    return str1
print("str反转后：",reversal(str))
#6
a=[1,2,3,4,5,6]
sum_a=sum(map(lambda x:x+3,a[1::2]))
print("列表中偶数加三在全部相加:",sum_a)
#7
List=[-2,1,3,-6]
for i in range(0,3):
    for j in range(i,4):
        if abs(List[i])>abs(List[j]):
            t=List[i]
            List[i]=List[j]
            List[j]=t
print("按绝对值从小到大排序：",List)
#8
List1=[1,2,3,4]
List2=[5,6,7,8]
for i in range(len(List2)):
    List1.append(List2[i])
print("合并后的列表：",List1)
#9
print("lambda函数是匿名函数，当实现的函数只需要一行时使用，方便简洁。")
#10
print("元组tuple不可变,列表list和字典dict可变。")
#11
alist=[
{'name':'a','age':20},
{'name':'b','age':30},
{'name':'c','age':25}]
for i in range(0,2):
    for j in range(i,3):
        if alist[i]['age']<alist[j]['age']:
            t=alist[i]
            alist[i]=alist[j]
            alist[j]=t
print("alist按age从大到小排序：",alist)
#12
str="k:1|k1:2|k2:3|k3:4"
str_list=str.split('|')
dict={}
for i in str_list:
lambda函数python
设置登录我的关注

    key,value=i.split(':')
    dict[key]=value
print(dict)
#13
n=25
fibonacci=[]
for i in range(n):
    if i==0:
        fibonacci.append(0)
    elif i==1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
print(fibonacci)
#14
class student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_bestgrade(self):
        return max(self.grade)
zz=student("zhangming",20,[69,88,100])
print(zz.get_name())
print(zz.get_age())
print(zz.get_bestgrade())
#15
class dictclass:
    def __init__(self,dict):
        self.dict=dict
    def del_dict(self,key):
        if key in self.dict:
            self.dict.pop(key)
            return self.dict
        else:
            return "no this key"
    def get_dict(self,key):
        if key in self.dict:
            return self.dict[key]
        else:
            return "not found"
    def get_key(self):
        return self.dict.keys()
    def update_dict(self,dict2):
        self.dict=dict(self.dict,**dict2)
        return self.dict.values()
A=dictclass({'a':1,'b':2,'c':3})
print(A.del_dict('c'))
print(A.get_dict('c'))
print(A.get_key())
print(A.update_dict({'c':3}))
#16
class Listinfo:
    def __init__(self,list):
        self.list=list
    def add_key(self,keyname):
        if isinstance(keyname,(int,str)):
            self.list.append(keyname)
            return self.list
        else:
            return "error"
    def get_key(self,num):
        if num>=0&num<len(self.list):
            return self.list[num]
        else:
            return "error"
    def update_list(self,list2):
        self.list.extend(list2)
        return self.list
    def del_key(self):
        del self.list[-1]
        return self.list
B=Listinfo([1,2,3,4,5])
print(B.add_key(6))
print(B.get_key(0))
print(B.update_list([7,8,9]))
print(B.del_key())
#17
class setinfo:
    def __init__(self,set):
        self.set=set
    def add_setinfo(self,keyname):
        if isinstance(keyname,(int,str)):
            self.set.add(keyname)
            return self.set
        else:
            return "error"
    def get_intersection(self,set2):
        if isinstance(set2,set):
            return self.set & set2
        else:
            return "error"
    def get_union(self,set2):
        if isinstance(set2,set):
            return self.set | set2
        else:
            return "error"
    def get_difference(self,set2):
        if isinstance(set2,set):
            return self.set - set2
C=setinfo({1,2,3})
D={4,5,6,7}
print(C.add_setinfo(4))
print(C.get_intersection(D))
print(C.get_union(D))
print(C.get_difference(D))
#18
class student:
    def __init__(self,name,sex,age,address):
        self.name=name
        self.sex=sex
        self.age=age
        self.address=address
    def display(self):
        print("姓名：{}\n性别：{}\n年龄：{}\n家庭地址：{}".format(self.name,self.sex,self.age,self.address))
mine=student('王成阳',"男",21,"乐山")
mine.display()
#19
class father:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def multiplicate(self):
        print(self.a*self.b)
class son(father):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print(self.a+self.b)
s1=son(1,2)
s1.sum()
s1.multiplicate()'''



# print(r"\r'")
# import cv2




# a=[1,2,3]
# print(a[1])
# print(a[000001])
# import numpy as np
#
# a=np.array([[1,2,3],[1,2]])
# print(a.shape)
# import numpy as np
# import numpy as py
# a=np.arange(12).reshape(4,3)
# b=np.arange(12).reshape(3,4)
# c=np.dot(a,b)
# print(c)

arr=eval(input())
print(type(arr))









































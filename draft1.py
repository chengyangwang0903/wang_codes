import numpy as np
# x=[[1,2],[3,4]]
# a=np.array(x)
# print(x)
# print(a)
# b=a.tolist()
# print(b)
# w=np.ndarray([3,4]).reshape(2,2,3)
# print(w)
# a=np.arange(12).reshape(3,4)
# print(a)
# b=a.copy()#这种方式a，c没有共用一个内存空间
# b[0,0]=99
# print(a)
# print(b)
# c=a#这种方式a，c共用一个内存空间
# c[0,0]=88
# print(a)
# print(c)
# a=np.arange(12).reshape(4,3)
# b=np.arange(6).reshape(2,3)
# c=np.vstack((a,b))
# print(c)
# a=np.arange(12).reshape(4,3)
# b=np.arange(8).reshape(4,2)
# c=np.hstack((a,b))
# print(c)

'''重点：图片随机采样(有一点小问题)'''
import numpy as np
import os
import PIL.Image as img
path_image=r"D:/img"
class Sample:
    def read_data(self):
        self.images_arr=[]
        for name in os.listdir(path_image):
            imgs=img.open(r"{}/{}".format(path_image,name))
            images=np.array(imgs)
            self.images_arr.append(images)
        #print(self.images_arr.shape)
        return self.images_arr
    def get_batch(self,set):
        self.read_data()
        self.get_arr=[]
        for i in range(set):
            num=np.random.randint(len(self.images_arr))
            self.get_arr.append(self.images_arr[num])
        self.get_arr=np.array(self.get_arr,dtype=object)
        return self.get_arr
sample=Sample()
print(sample.get_batch(1))
print(np.shape(sample.get_batch(1)))
print("完成！")














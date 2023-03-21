import numpy as np
#查看数组a1的属性
def check(a1):
    print(a1)  
    print("数据类型",type(a1))           #打印数组数据类型  
    print("数组元素数据类型：",a1.dtype) #打印数组元素数据类型  
    print("数组元素总数：",a1.size)      #打印数组尺寸，即数组元素总数  
    print("数组形状：",a1.shape)         #打印数组形状  
    print("数组的维度数目",a1.ndim)      #打印数组的维度数目

A=np.array([[1,-1,1,1,-1,1,0],[-2,-3,-5,0,0,0,0],[1,0,-2,2,-2,0,-1]])
check(A)


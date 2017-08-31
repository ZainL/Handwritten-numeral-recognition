import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

lena = mpimg.imread('2.png') # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
lena.shape #(512, 512, 3)
print(lena.shape)
plt.imshow(lena) # 显示图片
#plt.axis('on') # 不显示坐标轴
#plt.show()

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

gray = rgb2gray(lena)
# 也可以用 plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.imshow(gray, cmap='Greys_r')
for i in range(0,28):
    for j in range(0,28):
        print("i=",i)
        print("j=",j)
        print("gray[",i,"][",j,"]=",gray[i][j])
        if gray[i][j] == 1.0:
            print("---")
            gray[i][j] = 0.0
        print("gray[", i, "][", j, "]=", gray[i][j])

print(gray.shape)
print(gray)
plt.axis('on')
plt.show()
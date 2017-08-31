from __future__ import division, print_function, absolute_import

import numpy as np
from PIL import Image

class ImageData:
    def getArrayFromImage(self,file):
        # 读取图片转成灰度格式
        img = Image.open(file).convert('L')

        # resize的过程
        if img.size[0] != 28 or img.size[1] != 28:
            img = img.resize((28, 28))

        # 暂存像素值的一维数组
        arr = []

        for i in range(28):
            for j in range(28):
                # mnist 里的颜色是0代表白色（背景），1.0代表黑色
                pixel = 1.0 - float(img.getpixel((j, i))) / 255.0
                # pixel = 255.0 - float(img.getpixel((j, i))) # 如果是0-255的颜色值
                arr.append(pixel)

        arr1 = np.array(arr).reshape((784, 1))
        #print(arr1)
        #print(arr1.shape)
        #img.show()
        return arr1



"""
training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)

"""
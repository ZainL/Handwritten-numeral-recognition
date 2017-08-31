from PIL import Image
import numpy as np

class Data2:
    def getTestPicArray(self,filename):
        im = Image.open(filename)
        x_s = 28
        y_s = 28
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        im_arr = np.array(out.convert('L'))
        num0 = 0
        num255 = 0
        threshold = 100

        for x in range(x_s):
            for y in range(y_s):
                if im_arr[x][y] > threshold:
                    num255 = num255 + 1
                else:
                    num0 = num0 + 1

        if (num255 > num0):
            #print("convert!")
            for x in range(x_s):
                for y in range(y_s):
                    im_arr[x][y] = 255 - im_arr[x][y]
                    if (im_arr[x][y] < threshold):  im_arr[x][y] = 0
                    # if(im_arr[x][y] > threshold) : im_arr[x][y] = 0
                    # else : im_arr[x][y] = 255
                    # if(im_arr[x][y] < threshold): im_arr[x][y] = im_arr[x][y] - im_arr[x][y] / 2

        out = Image.fromarray(np.uint8(im_arr))
        out.save("C:\\Users\\Administrator\\Desktop\\out\\" + filename)
        # print im_arr                               
        nm = im_arr.reshape((1, 784))

        nm = nm.astype(np.float32)
        nm = np.multiply(nm, 1.0 / 255.0)

       # print(nm.reshape((784,1)).shape)
        #print(nm.shape)
        return nm.reshape((784,1))
    #   return nm

    #getTestPicArray(r"C:\Users\Administrator\Desktop\2.png")
#Data2().getTestPicArray(r"2.png")
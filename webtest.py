import web
#web.py库
import base64
#base64库，字符串<=>图片
import numpy as np
render = web.template.render('templates')
import network
#神经网络
import mnist_loader
#MINIST加载
net = network.Network([784, 30, 10])
#新建一个三层神经网络
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
#获得训练数据，验证数据，测试数据
training_data = list(training_data)

import mnist_data_loder
#自定义手写数据库加载

loder = mnist_data_loder.DataLoder()
#自定义手写数据库加载

#training_data = list()
urls = (
    '/index', 'index',
    '/Judge','judge',
    '/Join','join',
    '/static/(.*)','StaticFile' ,
    '/(.*.css)', 'StaticFile',  # 处理css文件
    '/(.*.js)', 'StaticFile',  # 处理js文件
    '/(.*)', 'hello'
)
#web.py URL映射
app = web.application(urls, globals())
#新建web应用

#如果是join请求，分发到此类处理
class join:
    def POST(self):
        print("join POST ")
        print("input:", web.input().get("dataURL"))
        print("input:",web.input().get("number"))
        number = (int)(web.input().get("number"))

        dataURL = str(web.input().get("dataURL"))
        base64_str = dataURL.replace("data:image/png;base64,", "")
        #获得手写图片的base64字符串
        #print(base64_str)

        ori_image_data = base64.b64decode(base64_str)
        #将base64字符串转换为图片数据

        import uuid
        #唯一随机数
        name = str(uuid.uuid1()) + ".jpg"
        fout = open(name, 'wb')
        fout.write(ori_image_data)
        fout.close()
        #将图片数据保存为图片文件

        import test4
        data = test4.Data2().getTestPicArray(name)
        #将图片文件进行压缩等处理，得到784*1数组

        #print("data.shape=",data.shape)

        training_result = self.vectorized_result(number)
        #将图片对应的正确分类转化为10*1向量
        #print("training_result.shape=", training_result.shape)
        #print("training_result=", training_result)

        loder.join(data,training_result)
        #将数据加入自定义加载器中
        training_data, validation_data, test_data = loder.zip()
        #使用自定义加载器将数据打包成MNIST格式
        training_data = list(training_data)


        import threading

        #t1 = threading.Thread(target=net.SGD, args=(training_data,30,10,3.0,test_data))
        #t1.start()
        #net.SGD(training_data,30,10,3.0,test_data=test_data)


        #TODO 尝试将手写数据写入文本文件，不再使用MNIST
        """
        len= 2
len data[0]= 784
data[0].shape= (784, 1)
len data[1]= 10
data[1].shape= (10, 1)
        """


        return "加入训练集并后台开始训练"
        """
        training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
        
        """

    def vectorized_result(self,j):
        """Return a 10-dimensional unit vector with a 1.0 in the jth
        position and zeroes elsewhere.  This is used to convert a digit
        (0...9) into a corresponding desired output from the neural
        network."""
        e = np.zeros((10, 1))
        e[j] = 1.0
        return e


class judge:
    def GET(self):
        print("judge GET")

    def POST(self):
        print("judge POST ")
        print("input:",web.input().get("dataURL"))
        dataURL = str(web.input().get("dataURL"))
        base64_str = dataURL.replace("data:image/png;base64,","")
        print(base64_str)


        ori_image_data = base64.b64decode(base64_str)

        import uuid
        name =  str(uuid.uuid1()) + ".jpg"
        fout = open(name, 'wb')
        fout.write(ori_image_data)
        fout.close()

        import test4
        data = test4.Data2().getTestPicArray(name)
        #print(data)

        print("开始训练，训练集有:",len(training_data))
        net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
        print("训练完成，开始预测")
        return "预测的结果为:",net.cjtest(data)

class StaticFile:
    def GET(self, file):
        print("调用StaticFile GET. file=",file)
        web.seeother('/static/'+file); #重定向

class index:
    def GET(self):
        html = open("index.html",encoding="utf-8")
        return html.read()

class hello:
    def GET(self, name):
        html = open("index.html", encoding="utf-8")
        return html.read()
        """
        print("name=", name)
        if not name:
            return render.hello2("welcome")
        # return open(r"hello2.html").read()
        return render.hello2(name)

        
        :param name: 
        :return: 
        """


if __name__ == "__main__":

    #net.SGD(training_data, 30, 10, 2.0, test_data=test_data)
    print("神经网络初始化完成，启动web服务中...")
    app.run()
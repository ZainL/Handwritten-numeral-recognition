
import pickle
import gzip

# Third-party libraries
import numpy as np

class DataLoder():
    def __init__(self):
        tr_d, va_d, te_d = self.load_data()
        #self.training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
        #self.training_results = [self.vectorized_result(y) for y in tr_d[1]]
        #以上是MNIST加载过程
        self.training_inputs = []
        self.training_results = []
        #自定义则清空
        #self.numbers = []

        #training_inputs = []
        #training_results = []
        import csv
        #导入csv模块，将数据以csv格式存储起来
        try:
            csv_reader = csv.reader(open('shouxie.csv', encoding='utf-8'))
            for row in csv_reader:
                if len(row) == 794:
                    # print(row)
                    # print(row[0:784])
                    # print(row[784:794])

                    input = []
                    for i in row[0:784]:
                        input.append(float(i))
                    result = []
                    for f in row[784:794]:
                        # print(f)
                        result.append(float(f))
                    print("input", input)
                    print("result", result)

                    inputs = np.zeros((784, 1))
                    for i in range(0, 784):
                        inputs[i] = input[i]
                    # print("inputs", inputs)

                    e = np.zeros((10, 1))
                    for i in range(0, 10):
                        e[i] = result[i]
                    # print("result'=", e)

                    self.training_inputs.append(inputs)
                    self.training_results.append(e)
        except:
            print("文件打开失败")
        print("从shouxie.csv中读入", len(self.training_inputs), "条数据")

        training_data = zip(self.training_inputs, self.training_results)


        print("初始化训练数据成功，现有",len(self.training_inputs),"条数据")



    def join2(self, training_input, number):
        self.training_inputs.append(training_input)
        self.numbers.append(number)
        print("加入训练数据成功，现有", len(self.training_inputs), "条数据")

        for training_input, training_result in zip(self.training_inputs, self.training_results):
            data = []
            for i in training_input:
                data.append(i[0])
            data.append(number)
            self.spamwriter.writerow(data)

    def join(self,training_input,training_result):
        self.training_inputs.append(training_input)
        self.training_results.append(training_result)
        print("加入训练数据成功，现有",len(self.training_inputs),"条数据")

        import csv
        with open('shouxie.csv', 'w+') as csvfile:
            spamwriter = csv.writer(csvfile, dialect='excel')
            for training_input,training_result in zip(self.training_inputs,self.training_results):
                data = []
                for i in training_input:
                    data.append(i[0])
                for j in training_result:
                    data.append(j[0])
                spamwriter.writerow(data)
                print("data",data)
        csvfile.close()
        print("训练数据已保存到文件中")

    def zip(self):
        tr_d, va_d, te_d = self.load_data()
        training_data = zip(self.training_inputs, self.training_results)

        validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
        validation_data = zip(validation_inputs, va_d[1])
        test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
        test_data = zip(test_inputs, te_d[1])
        return (training_data, validation_data, test_data)


    def load_data(self):

        training_inputs = []
        training_results = []
        import csv
        try:
            csv_reader = csv.reader(open('shouxie.csv', encoding='utf-8'))
            for row in csv_reader:
                if len(row) == 794:
                    # print(row)
                    # print(row[0:784])
                    # print(row[784:794])

                    input = []
                    for i in row[0:784]:
                        input.append(float(i))
                    result = []
                    for f in row[784:794]:
                        # print(f)
                        result.append(float(f))
                    print("input", input)
                    print("result", result)

                    inputs = np.zeros((784, 1))
                    for i in range(0, 784):
                        inputs[i] = input[i]
                    #print("inputs", inputs)

                    e = np.zeros((10, 1))
                    for i in range(0, 10):
                        e[i] = result[i]
                    #print("result'=", e)

                    training_inputs.append(inputs)
                    training_results.append(e)
        except:
            print("文件打开失败")
        print("从shouxie.csv中读入", len(training_inputs), "条数据")
        training_data = zip(training_inputs, training_results)

        f = gzip.open('mnist.pkl.gz', 'rb')
        #training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
        training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
        f.close()
        return (training_data, validation_data, test_data)

    def load_data_wrapper(self):
        tr_d, va_d, te_d = self.load_data()
        training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
        training_results = [self.vectorized_result(y) for y in tr_d[1]]
        training_data = zip(training_inputs, training_results)
        validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
        validation_data = zip(validation_inputs, va_d[1])
        test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
        test_data = zip(test_inputs, te_d[1])

        """
                for data in training_data:
            print("-------------一条数据---------------")
            print("len=", len(data))
            print("len data[0]=", len(data[0]))
            print("data[0].shape=",data[0].shape)
            print("len data[1]=", len(data[1]))
            print("data[1].shape=", data[1].shape)
            print("---------------------------------")
        """

        #print(training_data[0])
        return (training_data, validation_data, test_data)

    def vectorized_result(self,j):
        e = np.zeros((10, 1))
        e[j] = 1.0
        return e

    #load_data_wrapper()
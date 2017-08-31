"""
    Testing code for different neural network configurations.
    Adapted for Python 3.5.2

    Usage in shell:
        python3.5 test.py

    Network (network.py and network2.py) parameters:
        2nd param is epochs count
        3rd param is batch size
        4th param is learning rate (eta)

    Author:
        Michał Dobrzański, 2016
        dobrzanski.michal.daniel@gmail.com
"""

# ----------------------
# - read the input data:

import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
training_data = list(training_data)

import network
net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 2.0, test_data=test_data)

import image_data
import test4
for i in range(0,10):
    file = str(i)+".png"
    #data = image_data.ImageData().getArrayFromImage(file)
    data = test4.Data2().getTestPicArray(file)
    print("预测:",file,"的结果为",net.cjtest(data))
print("-----------------------------------------------------------------------")
for i in range(0,10):
    file = str(i)+".png"
    data = image_data.ImageData().getArrayFromImage(file)
    #data = test4.Data2().getTestPicArray(file)
    print("预测:",file,"的结果为",net.cjtest(data))
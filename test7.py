import numpy as np
import csv
class CO2_GTA:
    def __init__(self):
        self.co2 = []
        self.gta = []

    def load(self):
        try:
            csv_reader = csv.reader(open('gy826.csv', encoding='utf-8'))
            for row in csv_reader:
                #if len(row) == 2:
                print(row)
                self.co2.append(float(row[0]))
                self.gta.append(float(row[1]))
        except:
            print("文件打开失败")
        #print("从co2_gta.csv中读入", len(self.co2), "组数据")



test = CO2_GTA()
test.load()

import numpy as np
import csv
class CO2_GTA:
    def __init__(self):
        self.co2 = []
        self.gta = []

    def load(self):
        try:
            csv_reader = csv.reader(open('co2_gta.csv', encoding='utf-8'))
            for row in csv_reader:
                if len(row) == 2:
                    print(row)
                    self.co2.append(float(row[0]))
                    self.gta.append(float(row[1]))
        except:
            print("文件打开失败")
        print("从co2_gta.csv中读入", len(self.co2), "组数据")

    def getCO2Length(self):
        return len(self.co2)

    def getGTALength(self):
        return len(self.gta)

    def getCO2(self):
        return self.co2

    def getGTA(self):
        return self.gta

    def calculate(self,t):
        gta_t = -108.9638 + 0.3985 * self.gta[t - 1] + 0.2269*self.gta[t - 4] + \
           0.0981* self.gta[t - 4] + 0.0657 * self.gta[t - 8] - 0.0676 * self.gta[t - 9] + \
           0.4031*self.co2[t - 1] - 0.7299*self.co2[t - 4]+0.6638*self.co2[t - 8]
        self.gta.append(gta_t)

test = CO2_GTA()
test.load()
print(test.getGTALength())
print(test.getGTA())
test.calculate(test.getGTALength())
print(test.getGTALength())
print(test.getGTA())
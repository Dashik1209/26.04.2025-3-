import math

class ValueList:

    def __init__(self):
        self.__data = []  
        self.__sum = 0.0  
        self.__sum_sq = 0.0  
        self.__avg = 0.0  
        self.__sd = 0.0  
        self.__count = 0 

    def getElem(self, ind):
        if 0 <= ind < len(self.__data):
            return self.__data[ind]
        else:
            raise IndexError("Индекс за пределами списка")

    def setElem(self, ind, val):
        if 0 <= ind < len(self.__data):
            old_val = self.__data[ind]
            self.__data[ind] = val

            self.__sum += (val - old_val)
            self.__sum_sq += (val**2 - old_val**2)
            self.__avg = self.__sum / self.__count
            self.__sd = math.sqrt(self.__sum_sq / self.__count - self.__avg**2)
        else:
            raise IndexError("Индекс за пределами списка")

    def newElem(self, val):
        self.__data.append(val)
        self.__count += 1

        self.__sum += val
        self.__sum_sq += val**2
        self.__avg = self.__sum / self.__count
        self.__sd = math.sqrt(self.__sum_sq / self.__count - self.__avg**2)

    def getAvg(self):
        return self.__avg

    def getSD(self):
        return self.__sd




values.setElem(1, 25)

print(f"Новое среднее: {values.getAvg()}")  
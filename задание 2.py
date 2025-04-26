class Rectangle:

    def __init__(self, height, length):
        self.__height = height  
        self.__length = length  
        self.__square = self.__calculate_square()  
        self.__perimeter = self.__calculate_perimeter()  

    def getHigh(self):
        return self.__height

    def setHigh(self, height):
        self.__height = height
        self.__square = self.__calculate_square()
        self.__perimeter = self.__calculate_perimeter()

    def getLength(self):
        return self.__length

    def setLength(self, length):
        self.__length = length
        self.__square = self.__calculate_square()
        self.__perimeter = self.__calculate_perimeter()

    def getSquare(self):
        return self.__square

    def getPerimeter(self):
        return self.__perimeter

    def __calculate_square(self):
        return self.__height * self.__length

    def __calculate_perimeter(self):
        return 2 * (self.__height + self.__length)



rectangle.setHigh(8)
rectangle.setLength(12)

print(f"Новая высота: {rectangle.getHigh()}")  
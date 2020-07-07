class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def ashalt_mass(self):
        return self.__width * self.__length * 25 * 1

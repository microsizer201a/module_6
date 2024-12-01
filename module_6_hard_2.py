import math

class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filed = True

    def __init__(self, color, *sides):
        r, g, b = color
        self.set_color(r, g, b)
        if self.__is_valid_sides(sides):
            self.__sides = [side for side in sides]
        else:
            self.__sides = [1] * self.sides_count


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
       if (0, 0, 0) <= (r, g, b) <= (255, 255, 255):
           return True
       else:
           return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        is_positive = False
        for side in sides:

            if side > 0 or isinstance(side, int):
                is_positive = True
                break
            else:
                continue
        is_equal_ = False
        if len(sides) == self.sides_count:
            is_equal_ = True
        if is_positive and is_equal_:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        p = 0
        for i in self.__sides:
            p += i
        return p

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            count_ = 0
            for i in range(len(new_sides)):
                count_ += 1
            if self.sides_count == count_:
                self.__sides = [*new_sides]
            elif self.sides_count == 12 and count_ == 1:
                self.__sides = [new_sides[0] for i in range(self.sides_count)]
        elif len(self.__sides) < 1:
            self.__sides = [1 for i in range(self.sides_count)]

class Circle(Figure):

    def __init__(self, color, side):
        self.sides_count = 1
        super().__init__(color, side)
        self.__radius = len(self) / (2 * 3.14)

    def get_square(self):
        return 3.14 * self.__radius ** 2

class Triangle(Figure):

    def __init__(self, color, *sides):
        self.sides_count = 3
        super().__init__(color, *sides)


    def get_square(self):
        pp = len(self) / 2
        a, b, c = self.get_sides()
        return math.sqrt(pp * (pp - a) * (pp - b) * (pp - c))

class Cube(Figure):

    def __init__(self, color, *side):
        self.sides_count = 12
        if len(side) == 1 and side[0] > 0:
            sides = [side[0] for i in range(self.sides_count)]
            super().__init__(color, *sides)

    def get_volume(self):
        sides = self.get_sides()
        a = sides[0]
        v = a * a * a
        return v


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
triangle1 = Triangle((200, 200, 200), 10, 15)
print(triangle1.get_sides())
cube1 = Cube((222, 35, 130), 6)
print(cube1.get_sides())

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
triangle1.set_color(100, 100, 100)
print(circle1.get_color())
print(triangle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
triangle1.set_sides(15, 1, 10)
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
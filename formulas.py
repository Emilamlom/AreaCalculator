from math import pi

class Formulas:
    def circle(radius):
        '''
        Function to compute the area of a circle.
        :param radius: Radius of the circle
        :return: the circle's area
        '''
        try:
            radius = float(radius)
            if radius <= 0:
                raise ValueError('Values for area cannot be negative')
            else:
                return (radius ** 2) * pi
        except ValueError as e:
            return e

    def rectangle(length, width) -> float:
        '''
        Function to compute the area of a rectangle.
        :param length: Length of one side
        :param width: width of the other side
        :return: the rectangle's area
        '''
        try:
            length = float(length)
            width = float(width)
            if length <= 0 or width <= 0:
                raise ValueError('Values for area cannot be negative')
            else:
                return length * width
        except ValueError as e:
            return e
        except:
            return "Error"

    def square(side: float) -> float:
        '''
        Function to compute the area of a square.
        :param side: Length of one side
        :return: the square's area
        '''
        try:
            side = float(side)
            if side <= 0:
                raise ValueError('Values for area cannot be negative')
            else:
                return side ** 2
        except ValueError as e:
            return e
        except:
            return "Error"

    def triangle(base: float, height: float) -> float:
        '''
        Function to compute the area of a square.
        :param base: Length of the base of the triangle
        :param height: Height of the triangle
        :return: the triangle's area
        '''
        try:
            base = float(base)
            height = float(height)
            if base <= 0 or height <= 0:
                raise ValueError('Values for area cannot be negative')
            else:
                return (base * height)/2
        except ValueError as e:
            return e
        except:
            return "Error"

if __name__ == '__main__':
    Formulas.circle(-10)
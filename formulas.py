class Formulas:
    #TODO: Update formulas to return a value instead of printing it
    #TODO: Remove input statements and use parameters instead
    #TODO: Add documentation for each method
    def circle(radius):
        radius = float(radius)
        pi = 3.14159
        return (radius ** 2) * pi

    def rectangle(length, width):
        length = float(length)
        width = float(width)
        return length * width

    def square(side):
        side = float(side)
        return side ** 2

    def triangle(base, height):
        base = float(base)
        height = float(height)
        return (base * height)/2
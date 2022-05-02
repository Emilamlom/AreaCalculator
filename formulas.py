class Formulas:
    #TODO: Update formulas to return a value instead of printing it
    #TODO: Remove input statements and use parameters instead
    #TODO: Add documentation for each method
    def circle():
        radius = float(input("Circle Radius: "))
        pi = 3.14159
        area = (radius ** 2) * pi

        print(f'Circle Area = {area:.2f}')
        return

    def rectangle():
        length = float(input("Rectangle Length: "))
        width = float(input("Rectangle Width: "))

        area = length * width
        print(f'Rectangle Area = {area:.2f}')
        return


    def square():
        length = float(input("Square Side Length: "))

        area = length ** 2
        print(f'Square Area = {area:.2f}')
        return


    def triangle():
        base = float(input("Triangle base: "))
        height = float(input("Triangle height: "))

        area = (base * height)/2
        print(f'Triangle Area = {area:.2f}')
        return
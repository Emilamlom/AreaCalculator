from formulas import *
from gui import *

#TODO: Add GUI, remove input/print statements

def main():
    window = Tk()
    window.title('Area Calculator')
    window.geometry('450x300')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()

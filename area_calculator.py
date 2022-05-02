from gui import *

def main():
    window = Tk()
    window.title('Area Calculator')
    window.geometry('400x150')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()

from gui import *

def main():
    """
    Sets up the window parameters and call the GUI.
    """
    window = Tk()
    window.title('Area Calculator')
    window.geometry('400x150')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()

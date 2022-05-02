from tkinter import *

class GUI:
    def __init__(self, window):
        """
        Initializes the GUI
        """
        self.window = window

        self.formula_frame = Frame(self.window)
        self.formula_option = IntVar()
        self.formula_option.set(0)
        self.radio_circle = Radiobutton(self.formula_frame, text='Circle', variable=self.formula_option, value=0, command=self.circlesel).grid(column=0, row=0)
        self.radio_rect = Radiobutton(self.formula_frame, text='Rectangle', variable=self.formula_option, value=1, command=self.rectsel).grid(column=1, row=0)
        self.radio_square = Radiobutton(self.formula_frame, text='Square', variable=self.formula_option, value=2, command=self.squaresel).grid(column=2, row=0)
        self.radio_triangle = Radiobutton(self.formula_frame, text='Triangle', variable=self.formula_option, value=3, command=self.trianglesel).grid(column=3, row=0)

        self.circle_frame = Frame(self.window)
        self.radius_label = Label(self.circle_frame, text='Radius:', padx=5, pady=5).grid(column=0, row=0)
        self.radius_entry = Entry(self.circle_frame, width=10).grid(column=1, row=0)

        self.rect_frame = Frame(self.window)
        self.length_label = Label(self.rect_frame, text='Length:', padx=5, pady=5).grid(column=0, row=0)
        self.length_entry = Entry(self.rect_frame, width=10).grid(column=1, row=0)
        self.width_label = Label(self.rect_frame, text='Width:', padx=5, pady=5).grid(column=0, row=1)
        self.width_entry = Entry(self.rect_frame, width=10).grid(column=1, row=1)

        self.square_frame = Frame(self.window)
        self.side_label = Label(self.square_frame, text='Side length:', padx=5, pady=5).grid(column=0, row=0)
        self.side_entry = Entry(self.square_frame, width=10).grid(column=1, row=0)

        self.triangle_frame = Frame(self.window)
        self.base_label = Label(self.triangle_frame, text='Base length:', padx=5, pady=5).grid(column=0, row=0)
        self.base_entry = Entry(self.triangle_frame).grid(column=1, row=0)
        self.height_label = Label(self.triangle_frame, text='Height:', padx=5, pady=5).grid(column=0, row=1)
        self.height_entry = Entry(self.triangle_frame).grid(column=1, row=1)

        self.frame_calc = Frame(self.window).grid(column=1, row=1)
        self.button_calc = Button(self.frame_calc, text='Calculate', command=self.calcbutton, padx=5, pady=5)

    def circlesel(self):
        self.rect_frame.grid_forget()
        self.square_frame.grid_forget()
        self.triangle_frame.grid_forget()
        self.circle_frame.grid(row=1, column=0)

    def rectsel(self):
        self.circle_frame.grid_forget()
        self.square_frame.grid_forget()
        self.triangle_frame.grid_forget()
        self.rect_frame.grid(row=1, column=0)

    def squaresel(self):
        self.rect_frame.grid_forget()
        self.circle_frame.grid_forget()
        self.triangle_frame.grid_forget()
        self.square_frame.grid(row=1, column=0)

    def trianglesel(self):
        self.rect_frame.grid_forget()
        self.square_frame.grid_forget()
        self.circle_frame.grid_forget()
        self.triangle_frame.grid(row=1, column=0)

    def calcbutton(self):
        """
        Calls the correct calculate method and handles inputs/display
        """


        #self.entry_name.delete(0, 'end')
        #self.entry_age.delete(0, 'end')
        #self.radio_status.set(-1)
from tkinter import *
from formulas import *

class GUI:
    def __init__(self, window):
        """
        Initializes the GUI
        """
        self.window = window

        self.formula_frame = Frame(self.window)
        self.formula_frame.grid(column=0, row=0, columnspan=4)
        self.formula_option = IntVar()
        self.formula_option.set(0)
        self.radio_circle = Radiobutton(self.formula_frame, text='Circle', variable=self.formula_option, value=0, command=self.circlesel).grid(column=0, row=0)
        self.radio_rect = Radiobutton(self.formula_frame, text='Rectangle', variable=self.formula_option, value=1, command=self.rectsel).grid(column=1, row=0)
        self.radio_square = Radiobutton(self.formula_frame, text='Square', variable=self.formula_option, value=2, command=self.squaresel).grid(column=2, row=0)
        self.radio_triangle = Radiobutton(self.formula_frame, text='Triangle', variable=self.formula_option, value=3, command=self.trianglesel).grid(column=3, row=0)

        self.circle_frame = Frame(self.window)
        self.radius_label = Label(self.circle_frame, text='Radius:', padx=5, pady=5).grid(column=0, row=0)
        self.radius_entry = Entry(self.circle_frame, width=10)
        self.radius_entry.grid(column=1, row=0)

        self.rect_frame = Frame(self.window)
        self.length_label = Label(self.rect_frame, text='Length:', padx=5, pady=5).grid(column=0, row=0)
        self.length_entry = Entry(self.rect_frame, width=10)
        self.width_label = Label(self.rect_frame, text='Width:', padx=5, pady=5).grid(column=0, row=1)
        self.width_entry = Entry(self.rect_frame, width=10)
        self.length_entry.grid(column=1, row=0)
        self.width_entry.grid(column=1, row=1)

        self.square_frame = Frame(self.window)
        self.side_label = Label(self.square_frame, text='Side length:', padx=5, pady=5).grid(column=0, row=0)
        self.side_entry = Entry(self.square_frame, width=10)
        self.side_entry.grid(column=1, row=0)

        self.triangle_frame = Frame(self.window)
        self.base_label = Label(self.triangle_frame, text='Base length:', padx=5, pady=5).grid(column=0, row=0)
        self.base_entry = Entry(self.triangle_frame)
        self.height_label = Label(self.triangle_frame, text='Height:', padx=5, pady=5).grid(column=0, row=1)
        self.height_entry = Entry(self.triangle_frame)
        self.base_entry.grid(column=1, row=0)
        self.height_entry.grid(column=1, row=1)

        self.rect_frame.grid_forget()
        self.square_frame.grid_forget()
        self.triangle_frame.grid_forget()
        self.circle_frame.grid(row=1, column=0)

        self.calc_frame = Frame(self.window)
        self.calc_frame.grid(column=1, row=1, columnspan=2)
        self.button_calc = Button(self.calc_frame, text='Calculate', command=self.calcbutton, padx=5, pady=5, width=10).grid(column=0, row=0)

        self.result_frame = Frame(self.window)
        self.result_frame.grid(column=0, row=2, columnspan=4)

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        self.window.rowconfigure(1, weight=1)

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
        calcs = ['Circle', 'Rectangle', 'Square', 'Triangle']
        opt = self.formula_option.get()
        if opt == 0:
            result = Formulas.circle(self.radius_entry.get())
            self.radius_entry.delete(0, 'end')
        elif opt == 1:
            result = Formulas.rectangle(self.length_entry.get(), self.width_entry.get())
            self.width_entry.delete(0, 'end')
            self.length_entry.delete(0, 'end')
        elif opt == 2:
            result = Formulas.square(self.side_entry.get())
            self.side_entry.delete(0, 'end')
        elif opt == 3:
            result = Formulas.triangle(self.base_entry.get(), self.height_entry.get())
            self.height_entry.delete(0, 'end')
            self.base_entry.delete(0, 'end')

        self.label_result = Label(self.result_frame, text=f'{calcs[opt]} Area = {result}', padx=5, pady=5).grid(column=0, row=0)
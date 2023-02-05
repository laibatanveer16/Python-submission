from tkinter import *
import tkinter.messagebox as tmsg

def calculate():
    c = c_value.get()
    f = f_value.get()
    k = k_value.get()

    if c !=0:
        f = (c*(9/5)) + 32
        k = c + 273.15
        f_value.set(f)
        k_value.set(k)

    elif f != 0:
        c = (f-32) * (5/9)
        k = ((5/9) + f) + 459.67
        c_value.set(c)
        k_value.set(k)

    elif k != 0:
        c = k - 273.15
        f = ((k - 273.15) * (9/5)) + 32
        c_value.set(c)
        f_value.set(f)
    else:
        tmsg.showerror("Error","Enter 1 value and press calculate")

def show_formulas():
    show_root = Tk()
    show_root.title("FORMULA LIST")
    show_root.geometry("400x400")

    show_root.configure(bg = "powder blue")

    lbs = Label(show_root,
                bg = "powder blue",
                text="  FORMULA : ",
                font ="TimesNewRoman 20 bold underline",
                padx=20, pady=10)
    lbs.grid(row=0, column=4)

    lbs = Label(show_root,
                bg = "powder blue",
                text="\n CELSIUS CONVERSION:\n  \nF = (9/5 x C) + 32 \nK = C + 273.15 ",
                font ="Arial 10 bold",
                padx=5)

    lbs.grid(row=1, column=4)

    lbs = Label(show_root,
                bg = "powder blue",
                text="\n FAHRENHEIT CONVERSION:\n  \nC = (F - 32) x 5/9 \nK = (5/9 x F) + 459.67 ",
                font ="Arial 10 bold",
                padx=5)
    lbs.grid(row=2, column=4)

    lbs = Label(show_root,
                bg = "powder blue",
                text="\n KELVIN CONVERSION:\n \nC = K - 273.15 \nF = ((K - 273.15) x 9/5) + 32 ",
                font="comicsansms 10 bold",
                padx=5)
    lbs.grid(row=3, column=4)

    show_root.mainloop()

#TO RESET THE VALUES

def reset():
    c_value.set(0)
    f_value.set(0)
    k_value.set(0)

root = Tk()
root.title("TEMPERATURE CONVERTER")
root.geometry("600x500")
root.configure(bg="light blue")

lb = Label(root,
           text="TEMPERATURE CONVERTER",
           bg="lightblue", fg="black",
           font = "Arial 20 bold underline",
           padx=10, pady=20)
lb.grid(row=0,column=3)

lb_c = Label(root,
             text="Celsius",
             bg="lightblue", fg="black",
             font="Arial 14 ",
             padx=10, pady=10)
lb_c.grid(row=1, column=2)

lb_f = Label(root,
             text="Fahrenheit",
             bg="lightblue",  fg="black",
             font="Arial 14",
             padx=10, pady=10)
lb_f.grid(row=2, column=2)

lb_k = Label(root,
             text="Kelvin",
             bg="lightblue", fg="black",
             font="Arial 14",
             padx=10, pady=10)
lb_k.grid(row=3, column=2)

#TO GET THE DATA IN INT

c_value = IntVar()
f_value = IntVar()
k_value = IntVar()

#TO GET THE DATA OF CELSIUS
c_entry = Entry(root,textvariable=c_value)
c_entry.grid(row=1,column=3)

#TO GET THE DATA OF FAHRENHEIT
f_entry = Entry(root,textvariable=f_value)
f_entry.grid(row=2,column=3)

#TO GET DATA OF KELVIN
k_entry = Entry(root,textvariable=k_value)
k_entry.grid(row=3,column=3)

fr = Frame(root)
fr.grid(row=5,column=3)

#CREATING AN EMPTY LABEL TO GIVE SPACE
emptylabel = Label(bg="lightblue")
emptylabel.grid(row=4)

b_for_calculate = Button(fr,
                         text="Calculate",
                         command=calculate,
                         width=16)
b_for_calculate.grid(row=5, column=3)

#TO GIVE SPACE BETWEEN CALCULATE AND RESET
fr = Frame(root)
fr.grid(row=7,column=3)

#CREATING AN EMPTY LABEL TO GIVE SPACE
emptylabel2 = Label(bg="lightblue")
emptylabel2.grid(row=6)

b_to_reset = Button(fr,
                    text="Reset",
                    command=reset,
                    width=16)
b_to_reset.grid(row=7, column=3)

fr = Frame(root)
fr.grid(row=5,column=2)

b_to_show_formulas = Button(fr,
                            text="Show Conversion Formulas",
                            command=show_formulas)
b_to_show_formulas.grid(row=5, column=2)

root.mainloop()
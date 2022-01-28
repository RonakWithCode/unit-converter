from tkinter import *

unit_dict = {
    "cm" : 0.01,
    "m" : 1.0,
    "km": 1000.0,
    "feet": 0.3048,
    "miles": 1609.344,
    "inches": 0.0254,
    "grams" : 1.0,
    "kg" : 1000.0,
    "quintals": 100000.0,
    "tonnes" : 1000000.0,
    "pounds" : 453.592,
    "sq. m" : 1.0,
    "sq. km": 1000000.0,
    "are" : 100.0,
    "hectare" : 10000.0,
    "acre": 4046.856,
    "sq. mile" : 2590000.0,
    "sq. foot" : 0.0929,
    "cu. cm" : 0.001,
    "Litre" : 1.0,
    "ml" : 0.001,
    "gallon": 3.785
}

lengths = ["cm", "m", "km", "feet", "miles", "inches",]
weights = ["kg", "grams", "quintals", "tonnes", "pounds",]
temps = ["Celsius", "Fahrenheit"]
areas = ["sq. m", "sq. km", "are", "hectare", "acre", "sq. mile", "sq. foot"]
volumes = ["cu. cm", "Litre", "ml", "gallon"]

OPTIONS = ["select units",
            "cm",
            "m",
            "km",
            "feet",
            "miles",
            "inches",
            "kg",
            "grams",
            "quintals",
            "tonnes",
            "pounds",
            "Celsius",
            "Fahrenheit",
            "sq. m",
            "sq. km",
            "are",
            "hectare",
            "acre",
            "sq. mile",
            "sq. foot",
            "cu. cm",
            "Litre",
            "ml",
            "gallon"]
root = Tk()
root.geometry("400x350")
root.title("Unit Converter")

def unit():
    inp = float(inputentry.get())
    inp_unit = unit_input.get()
    out_unit = unit_output.get()

    cons = [inp_unit in lengths and out_unit in lengths,
    inp_unit in weights and out_unit in weights,
    inp_unit in temps and out_unit in temps,
    inp_unit in areas and out_unit in areas,
    inp_unit in volumes and out_unit in volumes]

    if any(cons):
        if inp_unit == "Celsius" and out_unit == "Fahrenheit":
            outputentry.delete(0, END)
            outputentry.insert(0, (inp * 1.8) + 32)
        elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
            outputentry.delete(0, END)
            outputentry.insert(0, (inp - 32) * (5/9))
        else:
            outputentry.delete(0, END)
            outputentry.insert(0, round(inp * unit_dict[inp_unit]/unit_dict[out_unit], 5))

    else:
        outputentry.delete(0, END)
        outputentry.insert(0, "ERROR")

unit_input = StringVar()
unit_input.set(OPTIONS[0])
unit_output = StringVar()
unit_output.set(OPTIONS[0])
inputentry = Entry(root, justify = "center", font = "bold")
inputentry.grid(row = 1, column = 0, padx = 35, ipady = 5)

inputmenu = OptionMenu(root, unit_input, *OPTIONS)
inputmenu.grid(row = 1, column = 1)
inputmenu.config(font = "Arial 10")
outputentry = Entry(root, justify = "center", font = "bold")
outputentry.grid(row = 3, column = 0, padx = 35, ipady = 5)

outputmenu = OptionMenu(root, unit_output, *OPTIONS)
outputmenu.grid(row = 3, column = 1)
outputmenu.config(font = "Arial 10")

okbtn = Button(root, text = "OK", command = unit, padx = 80, pady = 2)
okbtn.grid(row = 4, column = 0, columnspan = 2, pady = 50)

root.mainloop()
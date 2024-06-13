import FreeSimpleGUI as gui

def feet_to_inches(feet : int or float):
    inches = feet*12
    return inches

def inches_to_feet(inches : int or float):
    feet = feet/12
    return feet

def inches_and_feet_to_meteres(feet: int or float, inches: int or float)
    feet_meteres = feet* 0.3048
    inches_meteres = inches* 0.0254
    return f"{feet}ft -> {feet_meteres}m", f"{inches}in -> {inches_meteres}"

header = gui.Text("Enter feet:")
header2 = gui.Text("Enter inches:")

input_feet = gui.InputText(tooltip="Enter feet")
input_inches = gui.InputText(tooltip="Enter inches")
convert_button = gui.Button("Convert")
window = gui.Window("Converter", layout=[[header,input_feet],[header2,input_inches],[convert_button]])
window.read()
window.close()


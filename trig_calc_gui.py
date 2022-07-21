import PySimpleGUI as sg
import math

sg.theme('DarkTeal12')

font = ("Arial",11)

layout = [[sg.Text("Enter the length of two sides of a right\ntriangle to find the third\n"), sg.Image(source = r"C:\Users\rstack\Desktop\triangle.png", subsample=2)],
            [sg.Text("Enter Length of Side 1: ", size = (20,1)), sg.InputText()],
            [sg.Text("Enter Length of Side 2: ", size = (20,1)), sg.InputText()],
            [sg.Text("Enter Length of Hypotenuse: ", size = (20,1)), sg.InputText()],
            [sg.Text("\n")],
            [sg.Button("Calculate", size = (17,2))],
            [sg.Text("Measure of Angle 1 (deg): ", size = (20,1)), sg.InputText()],
            [sg.Text("Measure of Angle 2 (deg): ", size = (20,1)), sg.InputText()]]

window = sg.Window('Triangle Calculator',layout, font=font, element_justification='center')

def display_window():
    empty_spaces =[]
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Calculate":
            calcangles = True
            for key in values:
                if len(values[key]) == 0:
                    empty_spaces.append(key)
            if len(empty_spaces) > 3:
                window[3].update("INVALID")
                calcangles = False
            elif 1 in empty_spaces:
                answer = float(values[3])**2 - float(values[2])**2
                values[1] = math.sqrt(answer)
                window[1].update(math.sqrt(answer))
            elif 2 in empty_spaces:
                answer = float(values[3])**2 - float(values[1])**2
                values[2] = math.sqrt(answer)
                window[2].update(math.sqrt(answer))
            elif 3 in empty_spaces:
                answer = float(values[1])**2 + float(values[2])**2
                values[3] = math.sqrt(answer)
                window[3].update(math.sqrt(answer))
            empty_spaces=[]
            if calcangles:  #calculate angles using sin and cos
                window[4].update(values)
    
'''def display_window():
    empty_spaces =[]
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Calculate":
            count = 0
            for key in values:
                count +=1
                if len(values[key]) == 0:
                    empty_spaces.append(key)
            if len(empty_spaces) > 1:
                window[2].update("INVALID")
            elif 0 in empty_spaces:
                answer = float(values[2])**2 - float(values[1])**2
                window[0].update(math.sqrt(answer))
            elif 1 in empty_spaces:
                answer = float(values[2])**2 - float(values[0])**2
                window[1].update(math.sqrt(answer))
            elif 2 in empty_spaces:
                answer = float(values[0])**2 + float(values[1])**2
                window[2].update(math.sqrt(answer))
            empty_spaces=[]'''
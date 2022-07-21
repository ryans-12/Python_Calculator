import PySimpleGUI as sg


sg.theme('DarkTeal12')

font = ("Arial",11)

layout = [[sg.Text("Enter three values, then hit calculate to find the fourth.\n")],
            [sg.Text("Enter Initial Velocity (m/s): ", size= (20,1)), sg.InputText()],
            [sg.Text("Enter Acceleration (m/s^2): ",size= (20,1)), sg.InputText()],
            [sg.Text("Enter Time (s): ",size= (20,1)), sg.InputText()],
            [sg.Text("Enter Final Velocity (m/s): ",size= (20,1)), sg.InputText(key ="FV")],
            [sg.Text("")],
            [sg.Button("Calculate", size= (17,2))]]

window = sg.Window('Physics Calculator',layout, font=font, element_justification='center' ,size = (400,400))

def display_window(): 
    empty_spaces  =[]
    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Calculate":
            for key in values:
                if len(values[key]) == 0:
                    empty_spaces.append(key)
            if len(empty_spaces) > 1:
                window['FV'].update("INVALID")
            elif 0 in empty_spaces:
                answer = float(values['FV']) - (float(values[1]) * float(values[2]))
                window[0].update(answer)
            elif 1 in empty_spaces:
                answer = (float(values['FV']) - float(values[0]))/ float(values[2])
                window[1].update(answer)
            elif 2 in empty_spaces:
                answer = (float(values['FV']) - float(values[0]))/ float(values[1])
                window[2].update(answer)
            elif 'FV' in empty_spaces:
                answer = float(values[0]) + (float(values[1]) * float(values[2]))
                window['FV'].update(answer)
            empty_spaces = []

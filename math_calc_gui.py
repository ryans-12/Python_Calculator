import PySimpleGUI as sg

import phys_calc_gui as phys
import trig_calc_gui as trig

font = ("Arial",12)

sg.theme('DarkTeal12')


layout = [[sg.Text(size = (12,2),justification = 'center',text_color='black',background_color = 'white', key = 'display')],
        [sg.Button('+',size=(6,2)),sg.Button('-',size=(6,2)), sg.Button('x', size=(6,2)), sg.Button('/',size=(6,2))],
        [sg.Button('1', size = (9,2)),sg.Button('2',size = (9,2)),sg.Button('3',size = (9,2))],
        [sg.Button('4', size = (9,2)),sg.Button('5',size = (9,2)),sg.Button('6',size = (9,2))],
        [sg.Button('7', size = (9,2)),sg.Button('8',size = (9,2)),sg.Button('9',size = (9,2))],
        [sg.Button('0' , size = (9,2)),sg.Button('=' , size = (9,2)),sg.Button('C',size = (9,2))],
        [sg.Text("")],
        [sg.Button("Physics Calculator"), sg.Button("Triangle Calculator")]]

window = sg.Window('Math Calculator',layout,font=font, element_justification='center', size = (400,400))

answer = ''
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Physics Calculator":
        phys.display_window()
    elif event == "Triangle Calculator":
        trig.display_window()
    elif event == '=':
        final = round(eval(answer),8)
        final = str(final)
        answer = final
        window['display'].update(answer)
    elif event == 'C':
        answer = ""
        window['display'].update(answer)
    elif event == 'x':
        answer+='*'
        window['display'].update(answer)
    else:
        answer+= event
        window['display'].update(answer)

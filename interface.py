import PySimpleGUI as sg


#https://pysimplegui.readthedocs.io/en/latest/

#tema de cor
sg.theme('BrightColors')

#conteudo da janela
layout = [
            [sg.InputText('',size=(18,1))],
            [sg.Button('<-', size=(2,1)), sg.Button('yˣ', size=(2,1)), sg.Button('ˣ√y', size=(2,1)), sg.Button('/', size=(2,1))],
            [sg.Button('7', size=(2,1)), sg.Button('8', size=(2,1)), sg.Button('9', size=(2,1)), sg.Button('X', size=(2,1)),],
            [sg.Button('4', size=(2,1)), sg.Button('5', size=(2,1)), sg.Button('6', size=(2,1)), sg.Button('-', size=(2,1)),],
            [sg.Button('1', size=(2,1)), sg.Button('2', size=(2,1)), sg.Button('3', size=(2,1)), sg.Button('+', size=(2,1)),],
            [sg.Button('0', size=(2,1)), sg.Button('=', size=(11,1))]
            
            ]

# Create the Window
window = sg.Window('Calculadora MTST', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
#Agradecimento a todxs camaradas que me passaram cola pra esse projeto!
#ainda faltam alguns pontos mas já funciona

import PySimpleGUI as sg

def soma(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def texto_tela(valor):
    form['tela'].update(value=valor)

#tema de cor
sg.theme('BrightColors')

#conteudo da janela
layout = [
            [sg.InputText('', size=(18,1), key='tela')],
            [sg.ReadFormButton('<-'), sg.ReadFormButton('**'), sg.ReadFormButton('ˣ√y'), sg.ReadFormButton('/')],
            [sg.ReadFormButton(7), sg.ReadFormButton(8), sg.ReadFormButton(9), sg.ReadFormButton('*'),],
            [sg.ReadFormButton(4), sg.ReadFormButton(5), sg.ReadFormButton(6), sg.ReadFormButton('-'),],
            [sg.ReadFormButton(1), sg.ReadFormButton(2), sg.ReadFormButton(3), sg.ReadFormButton('+'),],
            [sg.ReadFormButton(0), sg.ReadFormButton('.'), sg.ReadFormButton('=', size=(11,1))]
            
            ]

#forma
form= sg.FlexForm('Calculadora do MTST', default_button_element_size=(2,1), auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)

# Event Loop to process "events" and get the "values" of the inputs
string_num = ''
string_num2 = ''
num1 = 0
num2 = 0

op_func = None
while True:
    print(num1)

    event, values = form.read()
    # texto_tela(event)
  
    if event == sg.WIN_CLOSED: # if user closes window
        break
    elif event in '1234567890.':
        string_num += event
        texto_tela(string_num)
    else:
        num2 = float(string_num)
        if op_func != None:
            num1 = op_func(num1, num2)
        else:
            num1 = num2

        if event == '+':
            op_func = soma
        elif event == '-':
            op_func = sub
        elif event == '*':
            op_func = mult
        elif event == '/':
            op_func = div
        elif event == '=':
            op_func = None

        string_num = ''
        texto_tela(str(num1))


form.close()
import PySimpleGUI as sg

sg.theme('DarkBrown4')
layout = [

            [sg.Text('IMC')],
            [sg.Text('Massa: '), sg.Input(key='-MASS-' , size=(5,1))],
            [sg.Text('Altura: '), sg.Input(key='-HEIGHT-' , size=(5,1))],
            [sg.Push(), sg.Button('Calcular'),sg.Push()]
         ]

window = sg.Window('IMC', layout, font='Monaco 20')
while True:
    event, value = window.read()
    print(event, value)
    Massa=float(value['-MASS-'])
    Altura=float(value['-HEIGHT-'])
    imc= Massa / (Altura**2)
    sg.Popup(f'Seu IMC é: {imc:.2f}',font='fixed 24')
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
